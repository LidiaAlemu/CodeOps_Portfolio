function saveCart(cart) {
  localStorage.setItem("cart", JSON.stringify(cart));
}

function loadCart() {
  try {
    const raw = localStorage.getItem("cart");
    return raw ? JSON.parse(raw) : [];
  } catch (err) {
    return [];
  }
}

const cart = [{ name: "Teff", qty: 2 }];
saveCart(cart);
const loaded = loadCart();
console.log(loaded);