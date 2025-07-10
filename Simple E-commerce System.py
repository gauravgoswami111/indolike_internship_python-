# Simple E-commerce System in Python

class Product:
    def __init__(self, pid, name, price):
        self.id = pid
        self.name = name
        self.price = price

class Store:
    def __init__(self):
        self.products = [
            Product(1, "Laptop", 750),
            Product(2, "Smartphone", 500),
            Product(3, "Headphones", 100),
            Product(4, "Book", 20)
        ]

    def display_products(self):
        print("\nAvailable Products:")
        for product in self.products:
            print(f"{product.id}. {product.name} - ${product.price}")

    def get_product_by_id(self, pid):
        for product in self.products:
            if product.id == pid:
                return product
        return None

class Cart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, product):
        self.items.append(product)
        print(f"{product.name} added to cart.")

    def view_cart(self):
        if not self.items:
            print("Cart is empty.")
            return
        print("\nCart Items:")
        total = 0
        for item in self.items:
            print(f"{item.name} - ${item.price}")
            total += item.price
        print(f"Total: ${total}")

    def checkout(self):
        if not self.items:
            print("Cart is empty. Add items before checkout.")
            return
        print("\n--- Checkout ---")
        self.view_cart()
        print("Thank you for your purchase!")
        self.items = []  # Empty the cart after checkout

def main():
    store = Store()
    cart = Cart()

    while True:
        print("\n--- Simple E-Commerce ---")
        print("1. View Products")
        print("2. Add Product to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            store.display_products()
        elif choice == '2':
            try:
                pid = int(input("Enter Product ID to add to cart: "))
                product = store.get_product_by_id(pid)
                if product:
                    cart.add_to_cart(product)
                else:
                    print("Invalid Product ID.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '3':
            cart.view_cart()
        elif choice == '4':
            cart.checkout()
        elif choice == '5':
            print("Thank you for visiting!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
