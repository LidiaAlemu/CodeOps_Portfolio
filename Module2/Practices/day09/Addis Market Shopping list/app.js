let items = [];

const form = document.querySelector("#add-form");
const nameInput = document.querySelector("#name");
const list = document.querySelector("#list");
const count = document.querySelector("#count");

function render() {
  
  list.innerHTML = "";

  
  const remaining = items.filter(item => !item.done).length;
  count.textContent = remaining + " items left";

  
  items.forEach(item => {
    const li = document.createElement("li");
    li.textContent = item.name;
    li.dataset.id = item.id;

   
    if (item.done) {
      li.classList.add("done");
    }

    
    const deleteBtn = document.createElement("button");
    deleteBtn.textContent = "×";
    deleteBtn.className = "del";

    li.append(deleteBtn);
    list.append(li);
  });
}


form.addEventListener("submit", function (e) {
  e.preventDefault();

  const name = nameInput.value.trim();
  if (name === "") return;

  items.push({
    id: Date.now(),
    name: name,
    done: false
  });

  nameInput.value = "";
  render();
});


list.addEventListener("click", function (e) {
  const li = e.target.closest("li");
  if (!li) return;

  const id = Number(li.dataset.id);

  if (e.target.matches(".del")) {
    // remove the item
    items = items.filter(item => item.id !== id);
  } else {
    // toggle bought / not bought
    const item = items.find(item => item.id === id);
    item.done = !item.done;
  }

  render();
});


render();