import tkinter as tk


class CheckoutPage:
    def __init__(self, cart):
        self.cart = cart

        self.window = tk.Tk()
        self.window.title("Checkout")

        # Create labels for the cart items
        item_labels = []
        for item, price, quantity in cart:
            item_label = tk.Label(
                self.window, text=f"{item}: ${price:.2f} x {quantity}")
            item_label.pack()
            item_labels.append(item_label)

        # Create a label for the total cost
        total_cost = sum([price * quantity for _, price, quantity in cart])
        total_label = tk.Label(self.window, text=f"Total: ${total_cost:.2f}")
        total_label.pack()

        # Add a button to confirm the purchase
        confirm_button = tk.Button(
            self.window, text="Confirm Purchase", command=self.confirm_purchase)
        confirm_button.pack()

        self.window.mainloop()

    def confirm_purchase(self):
        # Perform actions to confirm the purchase, such as updating a database or sending an email
        print("Purchase confirmed!")
        self.window.destroy()


# Example usage
cart = [("Shirt", 20.00, 2), ("Pants", 30.00, 1), ("Socks", 5.00, 3)]
checkout_page = CheckoutPage(cart)
