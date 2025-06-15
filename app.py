import streamlit as st

# Mock product list
products = [
    {"name": "Apples", "price": 1.5},
    {"name": "Bananas", "price": 0.8},
    {"name": "Milk", "price": 2.0},
    {"name": "Bread", "price": 2.5},
]

# Initialize cart in session
if "cart" not in st.session_state:
    st.session_state.cart = {}

st.title("🛒 Simple Grocery Store")

# Display products
st.subheader("Available Products")
for i, product in enumerate(products):
    col1, col2 = st.columns([3, 1])
    with col1:
        st.text(f"{product['name']} - ${product['price']:.2f}")
    with col2:
        qty = st.number_input(f"Qty_{i}", min_value=0, step=1, label_visibility="collapsed")
        if qty > 0:
            st.session_state.cart[product["name"]] = (qty, product["price"])

# Show cart
st.subheader("🧺 Your Cart")
if st.session_state.cart:
    total = 0
    for name, (qty, price) in st.session_state.cart.items():
        st.text(f"{name} x {qty} = ${qty * price:.2f}")
        total += qty * price
    st.success(f"Total: ${total:.2f}")
else:
    st.info("Your cart is empty.")

# Checkout
if st.button("Checkout"):
    if st.session_state.cart:
        st.success("✅ Order submitted! Thank you!")
        st.session_state.cart.clear()
    else:
        st.warning("Your cart is empty.")
