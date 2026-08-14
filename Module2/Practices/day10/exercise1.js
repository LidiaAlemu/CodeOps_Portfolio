async function getUsdToEtbRate() {
  const res = await fetch("https://api.exchangerate.host/latest?base=USD");
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  const data = await res.json();
  return data.rates.ETB;
}


getUsdToEtbRate().then(rate => console.log("1 USD =", rate, "ETB"));