// script.js

const searchInput = document.getElementById("searchInput");
const suggestionsBox = document.getElementById("suggestions");

searchInput.addEventListener("input", async function () {
    const query = this.value.trim();
    suggestionsBox.innerHTML = "";

    if (query.length === 0) return;

    try {
        const response = await fetch(`http://127.0.0.1:5000/suggestions?q=${encodeURIComponent(query)}`);
        const suggestions = await response.json();

        suggestions.forEach((suggestion) => {
            const suggestionDiv = document.createElement("div");
            suggestionDiv.textContent = suggestion;
            suggestionDiv.classList.add("suggestion-item");

            suggestionDiv.addEventListener("click", () => {
                localStorage.setItem("selectedBook", suggestion);
                window.location.href = "book.html";
            });

            suggestionsBox.appendChild(suggestionDiv);
        });
    } catch (error) {
        console.error("Error fetching suggestions:", error);
    }
});
