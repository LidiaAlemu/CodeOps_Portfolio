const state = {
    base: "ETB",
    rates: {},
    watchlist: [],
    amount: 100,
    currency: "USD",
}

const API = "https://open.er-api.com/v6/latest/ETB";

const status = document.querySelector("#status");
const select = document.querySelector("#currency");
const form = document.querySelector("#convert-form");
const amountinput = document.querySelector("#amount");
const result = document.querySelector("#result");
const addbtn = document.querySelector("#watch");
const watchlist = document.querySelector("#watchlist") 

async function loadRates() {
    status.textContent = "Loading rates...";
    try {
        const res = await fetch(API);
        if (!res.ok) {
            throw new Error(`HTTP error! status: ${res.status}`);
        }
        const data = await res.json();
        state.rates = data.rates;
        status.textContent = "";
        render();
    } catch (error) {
        console.error(error);
        status.textContent = "Error loading rates.";
    }
}

function render() {
    const codes = Object.keys(state.rates);
    select.innerHTML = codes
        .map(c => `<option value="${c}">${c}</option>`)
        .join("");

    select.value = state.currency;

    renderWatchlist();
}
