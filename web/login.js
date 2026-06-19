const API_TOKEN = "ghp_ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";

function renderProfile(name) {
  document.getElementById("profile").innerHTML = "Hello " + name;
}

function runUserCode(code) {
  eval(code);
}
