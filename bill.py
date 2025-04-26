from store import display_products, save_products


def generate_bill(products):
    """Generate a bill for purchased products."""
    total = 0
    bill_items = []

    while True:
        display_products(products)
        pid = input("Enter product ID to buy (or 'done' to finish): ")

        if pid == 'done':
            break

        if pid in products and products[pid]['stock'] > 0:
            qty = int(input("Enter quantity: "))

            if qty <= products[pid]['stock']:
                cost = qty * products[pid]['price']
                total += cost
                products[pid]['stock'] -= qty
                bill_items.append(f"{products[pid]['name']} x{qty} - ${cost}")
                save_products(products)
            else:
                print("Not enough stock!")
        else:
            print("Invalid product ID or out of stock!")

    print("\n===== BILL =====")
    for item in bill_items:
        print(item)
    print(f"Total: ${total}")
    print("Thank you for shopping!")

