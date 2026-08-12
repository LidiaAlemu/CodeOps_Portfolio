// 1: map, filter, reduce 
const prices = [250, 600, 180, 900];

const withVat = prices.map(p => p * 1.15);
const under1000 = withVat.filter(p => p < 1000);
const grandTotal = under1000.reduce((sum, p) => sum + p, 0);

console.log("VAT prices:", withVat);
console.log("Under 1000:", under1000);
console.log("Grand total:", grandTotal);

// 2: Object entries
const customer = { name: "Almaz Bekele", city: "Addis Ababa", balance: 1500 };

for (const [key, value] of Object.entries(customer)) {
  console.log(key, value);
}

// 3: Destructuring
const { name, city } = customer;
function greet({ name }) {
  return `Selam ${name}`;
}
console.log(greet(customer));

// 4: Spread update
const updatedCustomer = { ...customer, city: "Bahir Dar", phone: "0911" };
console.log("Original:", customer);
console.log("Updated:", updatedCustomer);



