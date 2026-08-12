# TeleBirr Transaction Report

A small report generator over a list of TeleBirr transactions for an Addis shop.

## Modules

- **transactions.js** = Exports the array of transaction objects.
- **report.js** = Exports summary functions:
  - `totalByType(txns, type)` = Filters and reduces transactions by type.
  - `formatReceipts(txns)` = Maps transactions to formatted receipt strings using destructuring.
- **app.js** = Imports data and functions, prints the report, and demonstrates a spread update.

