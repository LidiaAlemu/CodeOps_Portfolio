async function testErrors() {
 
  try {
    const res = await fetch("https://notavalidlink.invalid");
  } catch (err) {
    console.log("Network error caught:", err.message);
  }

 
  try {
    const res = await fetch("https://restcountries.com/v3.1/name/definitely-not-a-country");
    console.log("res.ok:", res.ok, "status:", res.status);
    if (!res.ok) throw new Error("Country not found");
    const data = await res.json();
  } catch (err) {
    console.log("HTTP error caught:", err.message);
  }
}

testErrors();