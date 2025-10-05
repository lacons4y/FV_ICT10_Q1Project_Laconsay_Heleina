from pyscript import document

# These are strings, used to show the opening and closing hours, as well as the restaurant and owner name.
restaurant_name = "Bento Cake"
owner_name = "Heleina"
business_hours = "8 AM - 5 PM"

# These are integers, used to display the year established and the price of the most popular item.
year_established = 2025
popular_item_price = 100

# This is a boolean; it is there to display whether or not delivery is available.
has_delivery = True

# Lists used to display product names available in the shop menu and the allergens that can be found in them.
product_names = [
    "Strawberry Matcha Bento Cake",
    "Choco Lava Bento Cake",
    "Peanut Butter Bento Cake",
    "Cookies and Cream Bento Cake",
    "Caramel Bento Cake"
]
common_allergens = ["Nuts", "Chocolate", "Egg"]

# Holds each cake flavor and its corresponding price in pesos.
menu_prices = {
    "Strawberry Matcha Bento Cake": 120,
    "Choco Lava Bento Cake": 100,
    "Peanut Butter Bento Cake": 100,
    "Cookies and Cream Bento Cake": 110,
    "Caramel Bento Cake": 100
}

# Lists common allergens found in the cakes to inform customers.
common_allergens = ["Nuts", "Chocolate", "Egg"]

# This is a floating-point, it is used to show the sales tax rate applied to every order (8%).
tax_rate = 0.08

# Dictionary linking each menu item ID (used in the order.html checkboxes) to its name and price, making it easy to match selections from the form.
prices = {
    "strawberry": ("Strawberry Matcha Bento Cake", 120),
    "choco": ("Choco Lava Bento Cake", 100),
    "peanut": ("Peanut Butter Bento Cake", 100),
    "cookies": ("Cookies and Cream Bento Cake", 110),
    "caramel": ("Caramel Bento Cake", 100)
}


def create_order(e):
    """
    Handles the process of creating a new order when the user clicks 'Submit'.
    It collects customer details, validates inputs, calculates totals, and 
    displays an order summary on the webpage.
    """

    # Retrieves input values entered by the user.
    name = document.getElementById("name").value.strip()
    address = document.getElementById("address").value.strip()
    contact = document.getElementById("contact").value.strip()

    # Clears any existing summary text before showing a new order result.
    document.getElementById("summary").textContent = ""

    # Validates that all customer details are filled out before continuing.
    if not name or not address or not contact:
        document.getElementById("summary").textContent = (
            "⚠️ Please fill in all customer details before placing your order."
        )
        return

    # This collects the list of menu items the user selected.
    items = [
        item_name for item_id, (item_name, price) in prices.items()
        if document.getElementById(item_id).checked
    ]

    # It is used to calculate the total cost of the items picked by the user.
    total = sum(
        price for item_id, (item_name, price) in prices.items()
        if document.getElementById(item_id).checked
    )

    # Creates a receipt of the order for display.
    order_summary = (
        f"""✅ Order created successfully!

Order for: {name}
Address: {address}
Contact: {contact}

Items Ordered: {", ".join(items)}
Total: ₱ {total:.2f}"""
        if items else "⚠️ No items selected. Please choose from the menu."
    )

    # Displays the final order summary text in the web interface.
    document.getElementById("summary").textContent = order_summary

    # Resets the form fields for the next potential order.
    for item_id in prices:
        document.getElementById(item_id).checked = False
    document.getElementById("name").value = ""
    document.getElementById("address").value = ""
    document.getElementById("contact").value = ""

