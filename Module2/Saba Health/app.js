const state = {
    tips: [],
    favorites: [],
    search: "",
    category: "All"
};


const tipsEl = document.querySelector("#tips");

const favoritesEl = document.querySelector("#favorites");

const favoriteCountEl = document.querySelector("#favorite-count");

const searchEl = document.querySelector("#search");

const categoriesEl = document.querySelector("#categories");

const statusEl = document.querySelector("#status");


const categories = [
    "All",
    "Nutrition",
    "Hydration",
    "Sleep",
    "Fitness",
    "Mental Wellness"
];


function renderCategories() {

    categoriesEl.innerHTML =
        categories.map(category => {

            const active =
                state.category === category
                    ? "active"
                    : "";

            return `
                <button
                    class="category-button ${active}"
                    data-category="${category}"
                >
                    ${category}
                </button>
            `;

        }).join("");
}


function getVisibleTips() {

    const searchTerm =
        state.search.trim().toLowerCase();

    return state.tips.filter(tip => {

        const matchesSearch =
            tip.title
                .toLowerCase()
                .includes(searchTerm) ||
            tip.summary
                .toLowerCase()
                .includes(searchTerm);

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
                <article
                    class="tip-card"
                    data-id="${tip.id}"
                >

                    <img
                        class="tip-image"
                        src="${tip.image}"
                        alt="${tip.title}"
                        loading="lazy"
                    >

                    <div class="tip-content">

                        <span class="tip-category">
                            ${tip.category}
                        </span>

                        <h3 class="tip-title">
                            ${tip.title}
                        </h3>

                        <p class="tip-summary">
                            ${tip.summary}
                        </p>

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

        favoritesEl.innerHTML = `
            <p class="empty-favorites"> You haven't saved any health tips yet. </p>
        `;

        return;
    }

    favoritesEl.innerHTML =
        state.favorites.map(id => {
            const tip =
                state.tips.find(
                    tip => tip.id === id
                );

            if (!tip) {
                return "";
            }

            return `
                <div
                    class="favorite-item"
                    data-id="${tip.id}"
                >

                    <p class="favorite-item-title"> ${tip.title} </p>

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


function saveFavorites() {

    localStorage.setItem(
        "sabaHealthFavorites",
        JSON.stringify(state.favorites)
    );
}


function loadFavorites() {

    const saved =
        localStorage.getItem(
            "sabaHealthFavorites"
        );

    if (saved) {

        state.favorites =
            JSON.parse(saved);
    }
}


async function loadHealthTips() {

    statusEl.textContent =
        "Loading health tips...";

    try {

        const response =
            await fetch("Data/health.json");

        if (!response.ok) {

            throw new Error(
                `HTTP error: ${response.status}`
            );
        }

        state.tips =
            await response.json();

        render();

    } catch (error) {

        console.error(error);

        statusEl.textContent =
            `Could not load health tips. Please try again.`;
    }
}


searchEl.addEventListener(
    "input",
    event => {

        state.search =
            event.target.value;

        renderTips();
    }
);


categoriesEl.addEventListener(
    "click",
    event => {

        const button =
            event.target.closest(
                ".category-button"
            );

        if (!button) {
            return;
        }

        state.category = button.dataset.category;

        render();
    }
);


tipsEl.addEventListener(
    "click",
    event => {

        const button =
            event.target.closest(
                '[data-action="favorite"]'
            );

        if (!button) {
            return;
        }

        const card =
            button.closest(".tip-card");

        const id =
            Number(card.dataset.id);

        const alreadyFavorite =
            state.favorites.includes(id);

        if (alreadyFavorite) {

            state.favorites =
                state.favorites.filter(
                    favoriteId => favoriteId !== id
                );

        } else {

            state.favorites.push(id);
        }

        saveFavorites();

        render();
    }
);


favoritesEl.addEventListener(
    "click",
    event => {

        const button =
            event.target.closest(
                '[data-action="remove"]'
            );

        if (!button) {
            return;
        }

        const favoriteItem =
            button.closest(".favorite-item");

        const id =
            Number(favoriteItem.dataset.id);

        state.favorites =
            state.favorites.filter(
                favoriteId => favoriteId !== id
            );

        saveFavorites();

        render();
    }
);


async function init() {

    loadFavorites();

    renderCategories();

    await loadHealthTips();
}


init();