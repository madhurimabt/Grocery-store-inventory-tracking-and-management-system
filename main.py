from store import load_products, display_products, add_product
from bill import generate_bill


def main():
    """Main function to run the grocery store system."""
    products = load_products()

    while True:
        print("\nGrocery Store Management System")
        print("1. Display Products")
        print("2. Add Product")
        print("3. Generate Bill")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_products(products)
        elif choice == '2':
            add_product(products)
        elif choice == '3':
            generate_bill(products)
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
