fetch("/api/products")
  .then(res => res.json())
  .then(data => render(data))
  .catch(err => console.error(err));

  //async/await version

  async function loadProducts() {
  try {
    const res = await fetch("/api/products");
    const data = await res.json();
    render(data);
  } catch (err) {
    console.error(err);
  }
}