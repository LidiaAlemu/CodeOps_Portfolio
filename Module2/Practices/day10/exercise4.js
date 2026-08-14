async function fetchFirstTwoInParallel() {
  const listRes = await fetch("https://restcountries.com/v3.1/region/africa");
  const list = await listRes.json();
  const firstTwo = list.slice(0, 2);

  const detailPromises = firstTwo.map(country =>
    fetch(`https://restcountries.com/v3.1/name/${country.name.common}`).then(res => res.json())
  );

  const details = await Promise.all(detailPromises);
  console.log(details);
}

fetchFirstTwoInParallel();