const PHONE = /^(?:\+251|0)9\d{8}$/;
const form = document.querySelector("#signup-form");
const nameInput = document.querySelector("#name");
const phoneInput = document.querySelector("#phone");
const errorMsg = document.querySelector("#error");
const countEl = document.querySelector("#count");

function loadSignups() {
  try {
    const raw = localStorage.getItem("signups");
    return raw ? JSON.parse(raw) : [];
  } catch (err) {
    return [];
  }
}

function saveSignups(signups) {
  localStorage.setItem("signups", JSON.stringify(signups));
}

function updateCount() {
  const signups = loadSignups();
  countEl.textContent = `Total signups: ${signups.length}`;
}

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

  const signups = loadSignups();
  signups.push({ name, phone });
  saveSignups(signups);

  form.reset();
  updateCount();
});


updateCount();