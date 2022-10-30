
const phantom_btn = document.getElementById("phantom_btn")


const getProvider = () => {
    if ('phantom' in window) {
      console.log("phantom true");
      const provider = window.phantom?.solana;

      if (provider?.isPhantom) {
        return provider;
      }
    }

    window.open('https://phantom.app/', '_blank');
    console.log("phantom false");
};
  
 const getPhantom = async () => {

   const provider = getProvider(); // see "Detecting the Provider"
  if (provider.isConnected) {
    provider.disconnect()
    phantom_btn.innerHTML ='Phantom'
    console.log("disconnected");
   }
  else {

    try {
      const resp = await provider.connect();
          phantom_btn.innerHTML = "Connected <img class='connect-img' width='21px' src='{%static 'img/phantom.png'%}'>"
      console.log(resp.publicKey.toString());
      // 26qv4GCcx98RihuK3c4T6ozB3J7L6VwCuFVc7Ta2A3Uo 
    } catch (err) {
      // { code: 4001, message: 'User rejected the request.' }
    }
  }
}





phantom_btn.addEventListener('click', getPhantom);