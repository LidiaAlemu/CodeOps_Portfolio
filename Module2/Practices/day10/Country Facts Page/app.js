const factsDiv = document.querySelector("#facts");
const input = document.querySelector("#country-input");
const searchBtn = document.querySelector("#search-btn");

function renderFact(label, value) {
  const p = document.createElement("p");
  p.className = "fact";
  p.textContent = `${label}: ${value}`;
  factsDiv.append(p);
}

async function showCountry(name) {
  factsDiv.textContent = "Loading…";

  try {
    const res = await fetch(`https://restcountries.com/v3.1/name/${name}`);
    if (!res.ok) throw new Error("Country not found");
    const [country] = await res.json();

    factsDiv.innerHTML = "";

    renderFact("Capital", country.capital[0]);
    renderFact("Population", country.population.toLocaleString());
    renderFact("Region", country.region);

    const currencyKey = Object.keys(country.currencies)[0];
    const currency = country.currencies[currencyKey];
    renderFact("Currency", `${currency.name} (${currency.symbol})`);

    const img = document.createElement("img");
    img.src = country.flags.png;
    img.alt = `Flag of ${country.name.common}`;
    img.className = "flag";
    factsDiv.append(img);

  } catch (err) {
    factsDiv.textContent = err.message;
  }
}

searchBtn.addEventListener("click", function() {
  const name = input.value.trim();
  if (name) showCountry(name);
});


showCountry("ethiopia");