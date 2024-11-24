document.addEventListener("DOMContentLoaded", () => {
  console.log("Page loaded successfully!");

  let cart = []; // Array to store cart items

  // Fetch JSON data and display grocery items
  fetch("grocery.json")
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      displayGroceryItems(data);
    })
    .catch((error) => console.error("Error loading JSON:", error));
});

// Function to display grocery items
function displayGroceryItems(data) {
  const container = document.getElementById("grocery-container");
  container.innerHTML = ""; // Clear any existing content

  Object.keys(data).forEach((category) => {
    // Create category heading
    const categoryHeading = document.createElement("h3");
    categoryHeading.textContent =
      category.charAt(0).toUpperCase() + category.slice(1);
    container.appendChild(categoryHeading);

    // Create Bootstrap card deck
    const row = document.createElement("div");
    row.classList.add("row", "g-3");

    data[category].forEach((item) => {
      const col = document.createElement("div");
      col.classList.add("col-md-4");

      col.innerHTML = `
          <div class="card h-100">
            <div class="card-body">
              <h5 class="card-title">${item.name}</h5>
              <p class="card-text">Price: ₹${item.price} per ${item.unit}</p>
              <button class="btn btn-primary w-100 add-to-cart" data-id="${item.id}" data-category="${category}" data-name="${item.name}" data-price="${item.price}">Add to Cart</button>
            </div>
          </div>
        `;
      row.appendChild(col);
    });

    container.appendChild(row);
  });

  // Attach event listeners to "Add to Cart" buttons
  document.querySelectorAll(".add-to-cart").forEach((button) => {
    button.addEventListener("click", (event) => {
      const { id, category, name, price } = event.target.dataset;
      addToCart({ id, category, name, price: parseFloat(price) });
    });
  });
}

// Function to add items to the cart
function addToCart(item) {
  const cartContainer = document.getElementById("cart-container");
  cartContainer.classList.remove("d-none");

  const existingItem = cart.find(
    (cartItem) => cartItem.id === item.id && cartItem.category === item.category
  );

  if (existingItem) {
    existingItem.quantity += 1; // Increase quantity if item already in cart
  } else {
    cart.push({ ...item, quantity: 1 }); // Add new item to cart
  }

  updateCart();
}

// Function to update the cart UI and total price
function updateCart() {
  const cartItemsContainer = document.getElementById("cart-items");
  const cartTotalElement = document.getElementById("cart-total");

  cartItemsContainer.innerHTML = ""; // Clear current cart items

  let total = 0;

  cart.forEach((item) => {
    total += item.price * item.quantity;

    const cartItem = document.createElement("li");
    cartItem.classList.add(
      "list-group-item",
      "d-flex",
      "justify-content-between",
      "align-items-center"
    );

    cartItem.innerHTML = `
        <div>
          ${item.name} - ₹${item.price} x ${item.quantity}
        </div>
        <div>
          <button class="btn btn-sm btn-secondary increase-qty" data-id="${item.id}" data-category="${item.category}">+</button>
          <button class="btn btn-sm btn-secondary decrease-qty" data-id="${item.id}" data-category="${item.category}">-</button>
          <button class="btn btn-sm btn-danger remove-item" data-id="${item.id}" data-category="${item.category}">Remove</button>
        </div>
      `;

    cartItemsContainer.appendChild(cartItem);

    // Attach event listeners
    cartItem
      .querySelector(".increase-qty")
      .addEventListener("click", (event) => {
        const { id, category } = event.target.dataset;
        adjustQuantity(id, category, 1);
      });

    cartItem
      .querySelector(".decrease-qty")
      .addEventListener("click", (event) => {
        const { id, category } = event.target.dataset;
        adjustQuantity(id, category, -1);
      });

    cartItem
      .querySelector(".remove-item")
      .addEventListener("click", (event) => {
        const { id, category } = event.target.dataset;
        removeFromCart(id, category);
      });
  });

  cartTotalElement.textContent = total.toFixed(2); // Update total price
}

// Function to adjust item quantity
function adjustQuantity(id, category, delta) {
  const item = cart.find(
    (cartItem) => cartItem.id === id && cartItem.category === category
  );

  if (item) {
    item.quantity += delta;
    if (item.quantity <= 0) {
      removeFromCart(id, category);
    } else {
      updateCart();
    }
  }
}

// Function to remove items from the cart
function removeFromCart(id, category) {
  cart = cart.filter((item) => !(item.id === id && item.category === category));
  updateCart();

  // Hide cart container if empty
  if (cart.length === 0) {
    document.getElementById("cart-container").classList.add("d-none");
  }
}
