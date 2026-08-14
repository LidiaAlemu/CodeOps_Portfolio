const output = document.querySelector("#output");
const loadBtn = document.querySelector("#load");

async function loadData() {
  output.textContent = "Loading…";
  try {
    const res = await fetch("https://restcountries.com/v3.1/name/ethiopia");
    if (!res.ok) throw new Error("HTTP error");
    const data = await res.json();
    output.textContent = data[0].name.common;
  } catch (err) {
    output.textContent = "Error: could not load data.";
  }
}

loadBtn.addEventListener("click", loadData);