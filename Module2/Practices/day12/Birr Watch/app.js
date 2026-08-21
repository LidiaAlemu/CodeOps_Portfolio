const state = {
    base: "ETB",
    rates: {},
    watchlist: [],
    amount: 100,
    currency: "USD",
    result:"",
}

const API = "https://open.er-api.com/v6/latest/ETB";
const KEY = "birrwatch";

const status = document.querySelector("#status");
const select = document.querySelector("#currency");
const form = document.querySelector("#convert-form");
const amountinput = document.querySelector("#amount");
const result = document.querySelector("#result");
const addbtn = document.querySelector("#watch");
const watchLi = document.querySelector("#watchlist") 

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
    result.textContent = state.result;

    renderWatchlist();
}

form.addEventListener("submit", (event) => {
    event.preventDefault();

    const amount = Number(amount.Input.value);

    if(!Number.isFinite(amount) || amount <= 0) {
        result.textContent = "Please enter a valid amount.";
        return;
    }

    state.amount = amount;
    state.currency = select.value;

    const rate = state.rates[state.currency];
    const converted = (amount * rate).toFixed(2);

    state.result = `${amount}ETB - ${state.currency}`;

    save();
    render();
});

addbtn.addEventListener("click", () => {
    const currency = select.value;
    if(state.watchlist.includes(currency)){
        return;
    }

    state.watchlist.push(currency);

    save();
    render();
});

function renderWatchlist(){
    if (state.watchlist.length === 0){
        watchLi.innerHTML = "<li>No currencies yet</li>";
        return;
    }

    watchLi.innerHTML = state.watchlist
        .map(currency => {
            const rate = state.rates[currency];
            return`
                <li data-c="${currency}">
                    <span> 1 ETB = ${rate} ${currency} </span>
                    <button class="rm" type="button"> x </button>
                </li>
            `;
        })
        .join("")
}

watchLi.addEventListener("click", (event) =>{
    if(!event.target.matches(".rm")){
        return;
    }

    const item = event.target.closest("li");
    const currency = item.dataset.c;

    state.watchlist = state.watchlist.filter(c => c !== currency);
    save();
    render();
});

function save(){
    localStorage.setItem(
        KEY,
        JSON.stringify({
            watchlist: state.watchlist,
            currency: state.currency,
            amount: state.amount,
            result: state.result,
        })
    );
}

function load() {
    const saved = localStorage.getItem(KEY);
    if(saved){
        return;
    }

    try {
        const data = JSON.parse(saved);
        Object.assign(state, data);
        amountInput.value = state.amount;
    } catch(error) {
        console.error("Failed to load saved data", error);
    }
}

async function init() {
    load();
    await loadRates();
    render();
}

init();
