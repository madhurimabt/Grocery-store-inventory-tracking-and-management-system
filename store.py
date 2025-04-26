import json

def load_products():
    """Load product data from JSON file."""
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_products(products):
    """Save product data to JSON file."""
    with open("data.json", "w") as file:
        json.dump(products, file, indent=4)

def display_products(products):
    """Display available products."""
    print("\nAvailable Products:")
    for pid, details in products.items():
        print(f"ID: {pid}, Name: {details['name']}, Price: ${details['price']}, Stock: {details['stock']}")

def add_product(products):
    """Add a new product to the store."""
    pid = input("Enter product ID: ")
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    stock = int(input("Enter stock quantity: "))
    products[pid] = {"name": name, "price": price, "stock": stock}
    save_products(products)
    print("Product added successfully!")
