let items = [];

const form = document.querySelector("#add-form");
const nameInput = document.querySelector("#name");
const priceInput = document.querySelector("#price");
const list = document.querySelector("#list");
const totalEl = document.querySelector("#total");

function render() {
  list.innerHTML = "";

  let total = 0;
  items.forEach(item => {
    total += item.price;

    const li = document.createElement("li");
    li.dataset.id = item.id;
    li.textContent = `${item.name} - ${item.price} ETB`;

    if (item.bought) {
      li.classList.add("bought");
    }

    const delBtn = document.createElement("button");
    delBtn.textContent = "×";
    delBtn.className = "del";
    li.append(delBtn);

    list.append(li);
  });

  totalEl.textContent = `Total: ${total} ETB`;
}

form.addEventListener("submit", function(e) {
  e.preventDefault();

  const name = nameInput.value.trim();
  const price = Number(priceInput.value);

  if (name === "" || price <= 0) return;

  items.push({
    id: Date.now(),
    name: name,
    price: price,
    bought: false
  });

  form.reset();
  render();
});

list.addEventListener("click", function(e) {
  if (e.target.matches(".del")) {
    const li = e.target.closest("li");
    const id = Number(li.dataset.id);
    items = items.filter(item => item.id !== id);
    render();
  } else {
    const li = e.target.closest("li");
    if (!li) return;
    const id = Number(li.dataset.id);
    const item = items.find(item => item.id === id);
    item.bought = !item.bought;
    render();
  }
});

render();