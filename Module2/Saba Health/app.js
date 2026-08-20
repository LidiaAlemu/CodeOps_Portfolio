const state = {
    tips: [],
    favorites: [],
    search: "",
    category: "All"
};

// ==================== Constants ====================
const STORAGE_KEY = "sabaHealthFavorites";
const EMAIL_REGEX = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

// ==================== DOM Elements ====================
const tipsEl = document.querySelector("#tips");
const favoritesEl = document.querySelector("#favorites");
const favoriteCountEl = document.querySelector("#favorite-count");
const searchEl = document.querySelector("#search");
const categoriesEl = document.querySelector("#categories");
const statusEl = document.querySelector("#status");
const subscribeForm = document.querySelector("#subscribe-form");
const nameInput = document.querySelector("#sub-name");
const emailInput = document.querySelector("#sub-email");
const formErrorEl = document.querySelector("#form-error");
const formSuccessEl = document.querySelector("#form-success");
const modal = document.querySelector("#tip-modal");
const modalTitle = document.querySelector("#modal-title");
const modalContent = document.querySelector("#modal-content");
const modalSource = document.querySelector("#modal-source");

// ==================== Data (categories) ====================
const categories = [
    "All",
    "Nutrition",
    "Hydration",
    "Sleep",
    "Fitness",
    "Mental Wellness"
];

// ==================== Render Functions ====================
function renderCategories() {
    categoriesEl.innerHTML = categories.map(category => {
        const active = state.category === category ? "active" : "";
        return `
            <button
                class="category-button ${active}"
                data-category="${category}"
                aria-pressed="${active === 'active'}"
            >
                ${category}
            </button>
        `;
    }).join("");
}

function getVisibleTips() {
    const searchTerm = state.search.trim().toLowerCase();
    return state.tips.filter(tip => {
        const matchesSearch =
            tip.title.toLowerCase().includes(searchTerm) ||
            tip.summary.toLowerCase().includes(searchTerm);
        const matchesCategory =
            state.category === "All" ||
            tip.category === state.category;
        return matchesSearch && matchesCategory;
    });
}

function renderTips() {
    const visibleTips = getVisibleTips();

    if (visibleTips.length === 0) {
        tipsEl.innerHTML = "";
        statusEl.textContent = "No health tips found. Try another search or category.";
        return;
    }

    statusEl.textContent = `${visibleTips.length} health tips`;

    tipsEl.innerHTML = visibleTips.map(tip => {
        const isFavorite = state.favorites.includes(tip.id);
        return `
            <article class="tip-card" data-id="${tip.id}">
                <img
                    class="tip-image"
                    src="${tip.image}"
                    alt="${tip.title}"
                    loading="lazy"
                    onerror="this.style.display='none'"
                >
                <div class="tip-content">
                    <span class="tip-category">${tip.category}</span>
                    <h3 class="tip-title">${tip.title}</h3>
                    <p class="tip-summary">${tip.summary}</p>
                    <div class="tip-actions">
                        <button
                            class="save-button"
                            data-action="favorite"
                            aria-label="${isFavorite ? "Remove from" : "Save to"} favorites"
                        >
                            ${isFavorite ? "♥ Saved" : "♡ Save"}
                        </button>
                        <button
                            class="view-button"
                            data-action="view"
                        >
                            View →
                        </button>
                    </div>
                </div>
            </article>
        `;
    }).join("");
}

function renderFavorites() {
    favoriteCountEl.textContent = state.favorites.length;

    if (state.favorites.length === 0) {
        favoritesEl.innerHTML = `<p class="empty-favorites">You haven't saved any health tips yet.</p>`;
        return;
    }

    favoritesEl.innerHTML = state.favorites.map(id => {
        const tip = state.tips.find(tip => tip.id === id);
        if (!tip) return "";
        return `
            <div class="favorite-item" data-id="${tip.id}">
                <p class="favorite-item-title">${tip.title}</p>
                <button
                    class="remove-button"
                    data-action="remove"
                    aria-label="Remove ${tip.title} from favorites"
                >
                    ♡
                </button>
            </div>
        `;
    }).join("");
}

function render() {
    renderCategories();
    renderTips();
    renderFavorites();
}

// ==================== Persistence ====================
function saveFavorites() {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(state.favorites));
}

function loadFavorites() {
    const saved = localStorage.getItem(STORAGE_KEY);
    if (saved) {
        try {
            state.favorites = JSON.parse(saved);
        } catch (e) {
            console.error("Failed to parse favorites", e);
            state.favorites = [];
        }
    }
}

// ==================== Data Loading ====================
async function loadHealthTips() {
    statusEl.textContent = "Loading health tips...";
    try {
        const response = await fetch("data/health.json");
        if (!response.ok) throw new Error(`HTTP error: ${response.status}`);
        state.tips = await response.json();
        render();
    } catch (error) {
        console.error(error);
        showError("Could not load health tips. Please try again.");
    }
}

function showError(message) {
    statusEl.innerHTML = `
        <span>${message}</span>
        <button id="retry" class="retry-button">Try again</button>
    `;
    document.querySelector("#retry").addEventListener("click", loadHealthTips);
}

// ==================== Event Listeners ====================
searchEl.addEventListener("input", event => {
    state.search = event.target.value;
    renderTips();
});

categoriesEl.addEventListener("click", event => {
    const button = event.target.closest(".category-button");
    if (!button) return;
    state.category = button.dataset.category;
    render();
});

tipsEl.addEventListener("click", event => {
    const button = event.target.closest("[data-action]");
    if (!button) return;

    const card = button.closest(".tip-card");
    if (!card) return;

    const id = Number(card.dataset.id);

    if (button.dataset.action === "favorite") {
        const alreadyFavorite = state.favorites.includes(id);
        if (alreadyFavorite) {
            state.favorites = state.favorites.filter(favId => favId !== id);
        } else {
            state.favorites.push(id);
        }
        saveFavorites();
        render();
    } else if (button.dataset.action === "view") {
        const tip = state.tips.find(tip => tip.id === id);
        if (tip) openModal(tip);
    }
});

favoritesEl.addEventListener("click", event => {
    const button = event.target.closest('[data-action="remove"]');
    if (!button) return;
    const favoriteItem = button.closest(".favorite-item");
    const id = Number(favoriteItem.dataset.id);
    state.favorites = state.favorites.filter(favId => favId !== id);
    saveFavorites();
    render();
});

// ==================== Subscription Form ====================
function validateForm(name, email) {
    if (!name.trim()) return "Please enter your name.";
    if (!EMAIL_REGEX.test(email.trim())) return "Please enter a valid email address.";
    return "";
}

subscribeForm.addEventListener("submit", event => {
    event.preventDefault();
    const name = nameInput.value;
    const email = emailInput.value;
    const errorMsg = validateForm(name, email);
    formErrorEl.textContent = errorMsg;
    if (errorMsg) return;

    // Simulate successful subscription
    const subscription = {
        name: name.trim(),
        email: email.trim(),
        subscribedAt: new Date().toISOString()
    };
    console.log("Subscription:", subscription);

    // Clear form and show success
    subscribeForm.reset();
    formSuccessEl.hidden = false;
    formSuccessEl.textContent = "Thank you for subscribing! Check your email for daily tips.";
    setTimeout(() => {
        formSuccessEl.hidden = true;
    }, 5000);
});

// ==================== Modal ====================
function openModal(tip) {
    modalTitle.textContent = tip.title;
    modalContent.textContent = tip.content || "No additional information available.";
    modalSource.textContent = tip.source ? `Source: ${tip.source}` : "";
    modal.hidden = false;
    document.body.style.overflow = "hidden"; // Prevent background scroll
}

function closeModal() {
    modal.hidden = true;
    document.body.style.overflow = "";
}

modal.addEventListener("click", event => {
    if (event.target.dataset.action === "close-modal") {
        closeModal();
    }
});

document.addEventListener("keydown", event => {
    if (event.key === "Escape" && !modal.hidden) {
        closeModal();
    }
});

// ==================== Init ====================
async function init() {
    loadFavorites();
    renderCategories();
    await loadHealthTips();
}

init();