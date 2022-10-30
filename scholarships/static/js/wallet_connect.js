const martian_btn = document.getElementById("martian_btn");
let martian = false;
const toggleMartian = () => {
  martian ? disconnect() : getMartian();
}
const getProvider = () => {
  if ("martian" in window) {
    console.log("martian")
    
    return (window.martian);

  }
  window.open("https://www.martianwallet.xyz/", "_blank");
};

const getMartian = async () => {

  const provider = getProvider();
  console.log("detected"); 
  if (provider.isConnected) {
    try {
      const resp = await provider.connect();
      martian_btn.style.background = '#19ab6e';
      martian_btn.innerText = "wallet connected"
      walletAddress = resp.address.toString();

      martian = true

    } catch (error) {
      
    }
  } 


}

const disconnect = async () => {
  const provider = getProvider()
  await provider.disconnect();
  martian_btn.style.background = '#4d1426';
  martian_btn.innerText = "wallet disconnected"
  console.log("disconnected");
  martian = false;
}

martian_btn.addEventListener('click', toggleMartian);
