import tkinter as tk
from tkinter import messagebox

class Product:
    def _init_(self, name, price):
        self.name = name
        self.price = price

class Category:
    def _init_(self, name, products):
        self.name = name
        self.products = products

class ShoppingCart:
    def _init_(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def remove_item(self, product):
        self.items.remove(product)

    def calculate_total(self):
        total = sum(product.price for product in self.items)
        return total

class ShoppingCartApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Shopping Cart App")

        self.cart = ShoppingCart()

        self.categories = [
            Category("art_supplies", [
                Product("Paint Brushes", 5.99),
                Product("Canvas", 12.99),
                Product("Watercolor Set", 24.99),
                Product("Sketchbook", 8),
                Product("Acrylic Paints", 12)
            ])
        ]

        self.category_label = tk.Label(root, text="Select a category:")
        self.category_label.pack()

        self.category_var = tk.StringVar()
        self.category_var.set(self.categories[0].name)  
        self.category_menu = tk.OptionMenu(root, self.category_var, *[category.name for category in self.categories])
        self.category_menu.pack()

        self.product_frame = tk.Frame(root)
        self.product_frame.pack()

        self.add_button = tk.Button(root, text="Add to Cart", command=self.add_to_cart)
        self.add_button.pack()

        self.view_cart_button = tk.Button(root, text="View Cart", command=self.view_cart)
        self.view_cart_button.pack()

        self.checkout_button = tk.Button(root, text="Checkout", command=self.checkout)
        self.checkout_button.pack()

        self.exit_button = tk.Button(root, text="Exit", command=root.quit)
        self.exit_button.pack()

        self.update_products()

    def update_products(self):
        selected_category_name = self.category_var.get()
        selected_category = next(category for category in self.categories if category.name == selected_category_name)
        
        for widget in self.product_frame.winfo_children():
            widget.destroy()

        for product in selected_category.products:
            product_frame = tk.Frame(self.product_frame)
            product_label = tk.Label(product_frame, text=f"{product.name} - ${product.price:.2f}")
            add_button = tk.Button(product_frame, text="Add to Cart", command=lambda p=product: self.add_to_cart(p))
            product_label.pack(side=tk.LEFT)
            add_button.pack(side=tk.LEFT)
            product_frame.pack()

    def add_to_cart(self, product):
        self.cart.add_item(product)
        messagebox.showinfo("Added to Cart", f"{product.name} added to cart.")

    def view_cart(self):
        cart_contents = "Items in cart:\n"
        for idx, product in enumerate(self.cart.items, start=1):
            cart_contents += f"{idx}. {product.name} - ${product.price:.2f}\n"
        cart_contents += f"Total: ${self.cart.calculate_total():.2f}"
        messagebox.showinfo("Cart Contents", cart_contents)

    def checkout(self):
        total = self.cart.calculate_total()
        messagebox.showinfo("Checkout", f"Total: ${total:.2f}\nThank you for shopping!")

        self.cart.items.clear()
        self.view_cart()

if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingCartApp(root)
    root.mainloop()
