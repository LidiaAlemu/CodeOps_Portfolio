
const subtotal = (...prices) => prices.reduce((sum, price) => sum + price, 0);
const discountBy = rate => amount => amount * (1 - rate);
const withVat = amount => amount * 1.15;
const toETB = amount => `${amount.toFixed(2)} ETB`;


const makeReceiptMaker = (defaultDiscount = 0) => {
  let orderNumber = 0;
  return (prices, discountRate = defaultDiscount) => {
    orderNumber += 1;
    const sub = subtotal(...prices);
    const afterDiscount = discountBy(discountRate)(sub);
    const total = withVat(afterDiscount);
    return `#${orderNumber}: ${toETB(total)}`;
  };
};


const receipt = makeReceiptMaker(0.1);  

console.log(receipt([10, 20, 30]));   
console.log(receipt([50], 0));      
console.log(receipt([100, 50]));     

const another = makeReceiptMaker(0);
console.log(another([80]));          