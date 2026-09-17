let cart = [];

const countElement = document.getElementById("cartCount");
const toast = document.getElementById("toast");

function updateCartCount() {
    const total = cart.reduce((sum, item) => sum + item.quantity, 0);
    countElement.textContent = total;
}

function showToast(productName) {
    toast.textContent = `${productName} adicionado ao carrinho.`;
    toast.classList.add("show");
    setTimeout(() => toast.classList.remove("show"), 1800);
}

document.querySelectorAll(".add-button").forEach((button) => {
    button.addEventListener("click", () => {
        const id = Number(button.dataset.id);
        const existing = cart.find((item) => item.id === id);

        if (existing) {
            existing.quantity += 1;
        } else {
            cart.push({
                id,
                name: button.dataset.name,
                price: Number(button.dataset.price),
                quantity: 1
            });
        }

        updateCartCount();
        showToast(button.dataset.name);
    });
});

document.getElementById("cartButton")?.addEventListener("click", () => {
    if (cart.length === 0) {
        toast.textContent = "Seu carrinho está vazio.";
    } else {
        const total = cart.reduce((sum, item) => sum + item.price * item.quantity, 0);
        toast.textContent = `${cart.length} produto(s) • R$ ${total.toFixed(2).replace(".", ",")}`;
    }
    toast.classList.add("show");
    setTimeout(() => toast.classList.remove("show"), 2200);
});
