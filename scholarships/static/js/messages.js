const messages = document.getElementById("message");

const closeAlert = () => {
  messages.classList.add("display__alert");
};
const alertTimeout = setTimeout(closeAlert, 2000);