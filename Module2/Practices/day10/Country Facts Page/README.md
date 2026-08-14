# Country Facts Page

A simple single-page app that fetches live country data from the REST Countries API and displays facts like capital, population, region, currency, and flag.

## How to run

1. Open `index.html` in a web browser.
2. The page loads facts for **Ethiopia** by default.
3. Type another country name and click **Search**.

## API used

- [REST Countries](https://restcountries.com/) — `https://restcountries.com/v3.1/name/{country}`

## Features

- Loading state while fetching data
- Friendly error message when a country is not found
- Population formatted with commas
- Flag image displayed
- Uses `async/await`, `fetch`, and DOM methods