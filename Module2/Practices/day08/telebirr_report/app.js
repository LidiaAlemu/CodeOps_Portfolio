import { transactions } from "./transaction.js";
import { totalByType, formatReceipts } from "./report.js";

const creditTotal = totalByType(transactions, "credit");
const debitTotal = totalByType(transactions, "debit");
const receipts = formatReceipts(transactions);

console.log("TeleBirr Transaction Report");
console.log("Receipts:");
receipts.forEach(receipt => console.log(receipt));
console.log(`Total Credits: ${creditTotal} ETB`);
console.log(`Total Debits: ${debitTotal} ETB`);


const original = transactions[0];
const corrected = { ...original, amount: 300 };
console.log("Original transaction:", original);
console.log("Corrected transaction:", corrected);