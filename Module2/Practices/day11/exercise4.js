const PHONE = /^(?:\+251|0)9\d{8}$/;

form.addEventListener("submit", function(e) {
  e.preventDefault();

  const name = nameInput.value.trim();
  const phone = phoneInput.value.trim();

  let error = "";
  if (name.length < 2) {
    error = "Enter your full name.";
  } else if (!PHONE.test(phone)) {
    error = "Enter a valid Ethiopian phone number.";
  }

  if (error) {
    errorMsg.textContent = error;
    return;
  }

  errorMsg.textContent = "";
  
});