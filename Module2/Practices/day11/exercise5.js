form.addEventListener("submit", function(e) {
  e.preventDefault();

  const name = nameInput.value.trim();
  const phone = phoneInput.value.trim();

  if (name.length < 2) {
    errorMsg.textContent = "Name must be at least 2 characters.";
    return;
  }

  if (!PHONE.test(phone)) {
    errorMsg.textContent = "Phone must be 09xxxxxxxx or +2519xxxxxxxx.";
    return;
  }

  errorMsg.textContent = "";
});