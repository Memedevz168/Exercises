class Product:
    def __init__(self, name, price, quantity):
        # INITIALIZE THE PRODUCT WITH NAME, PRICE, AND QUANTITY
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        # REPRESENT THE PRODUCT WITH A STRING THAT SHOWS THE NAME, PRICE, AND QUANTITY
        return f"{self.name} (Price: ${self.price}, Quantity: {self.quantity})"


class ShoppingCart:
    def __init__(self):
        # INITIALIZE AN EMPTY CART
        self.cart = []

    def add_product(self, product, quantity):
        # CHECK IF THE REQUESTED QUANTITY IS AVAILABLE
        if quantity > product.quantity:
            print(f"Error: Only {product.quantity} {product.name}(s) are available in stock.")
            return

        # ADD A PRODUCT TO THE CART OR UPDATE ITS QUANTITY
        for item in self.cart:
            if item.name == product.name:
                item.quantity += quantity
                print(f"{product.name} quantity updated to {item.quantity}.")
                return
        
        # ADD A NEW ENTRY IN THE CART WITH THE SPECIFIED QUANTITY
        self.cart.append(Product(product.name, product.price, quantity))
        print(f"{product.name} added to the cart.")

    def remove_product(self, product_name):
        # REMOVE A PRODUCT BASED ON ITS NAME
        for item in self.cart:
            if item.name == product_name:
                self.cart.remove(item)
                print(f"{product_name} has been removed from the cart.")
                return
        print(f"Product {product_name} not found in the cart.")

    def total_price(self):
        # CALCULATE THE TOTAL PRICE OF ALL PRODUCTS IN THE CART
        return sum(item.price * item.quantity for item in self.cart)

    def display_cart(self):
        # DISPLAY ALL PRODUCTS IN THE CART
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("Shopping Cart Contents:")
            for item in self.cart:
                print(item)

    def checkout(self):
        # PERFORM THE CHECKOUT AND DISPLAY TOTAL PRICE
        if not self.cart:
            print("Your cart is empty, add products before checking out.")
        else:
            print("Proceeding to checkout...")
            self.display_cart()
            print(f"\nTotal Price: ${self.total_price()}")
            print("Thank you for shopping with us!")


# DISPLAY AVAILABLE PRODUCTS AND LET USER SELECT ONE
def display_products(products):
    print("\nAvailable Products:")
    for idx, product in enumerate(products, start=1):
        print(f"{idx}. {product.name} - ${product.price} (In stock: {product.quantity})")


def get_product_choice(products):
    while True:
        try:
            # ASK USER TO CHOOSE A PRODUCT FROM THE LIST
            choice = int(input("\nEnter the number of the product you'd like to add to your cart: "))
            if 1 <= choice <= len(products):
                return products[choice - 1]
            else:
                print("Invalid choice, please select a valid product number.")
        except ValueError:
            print("Invalid input, please enter a number.")


# TESTING THE SHOPPING CART SYSTEM
if __name__ == "__main__":
    # CREATE PRODUCT INSTANCES
    product1 = Product("Laptop", 1000, 5)
    product2 = Product("Phone", 500, 10)
    product3 = Product("Headphones", 150, 15)

    # CREATE A SHOPPING CART INSTANCE
    cart = ShoppingCart()

    # CREATE A LIST OF AVAILABLE PRODUCTS
    available_products = [product1, product2, product3]

    # LET USER SELECT A PRODUCT TO ADD TO THE CART
    display_products(available_products)
    selected_product = get_product_choice(available_products)

    # ASK THE USER HOW MANY OF THE SELECTED ITEM THEY WANT TO ADD
    while True:
        try:
            quantity = int(input(f"How many {selected_product.name}s would you like to add to the cart? "))
            if quantity > 0:
                break
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # ADD PRODUCT TO THE CART WITHOUT MODIFYING ORIGINAL STOCK
    cart.add_product(selected_product, quantity)

    # DISPLAY THE CART CONTENTS
    print("\nDisplaying cart contents:")
    cart.display_cart()

    # DISPLAY THE TOTAL PRICE
    print(f"\nTotal Price: ${cart.total_price()}")

    # REMOVE A PRODUCT FROM THE CART
    cart.remove_product("Phone")

    # DISPLAY THE CART AFTER REMOVAL
    print("\nCart after removal of Phone:")
    cart.display_cart()

    # DISPLAY UPDATED TOTAL PRICE
    print(f"\nUpdated Total Price: ${cart.total_price()}")

    # PERFORM CHECKOUT
    cart.checkout()
s