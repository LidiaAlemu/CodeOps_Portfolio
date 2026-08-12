// 5: Module

// app.js
import { VAT, addVat } from "./money.js";
const price = 200;
console.log(`Price with VAT: ${addVat(price)}`);