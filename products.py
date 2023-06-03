class Product:
    """Creates a product object with the name, price, and quantity of it"""

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        if self.name == "":
            raise Exception
        if self.price < 0 or self.quantity < 0:
            raise Exception

    def is_active(self):
        """Return the activation status of the product"""
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        """Establishes the quantity of the product and depending on this one, it deactivates the product"""
        self.quantity = quantity
        if self.quantity <= 0:
            self.deactivate()

    def show(self):
        """Displays the basic information of the product"""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        """Checks whether the number of products bought is not over the
        available products, if so, raises a excpetion, and in case all
        matches correctly, it rests the quantity of products bought to the total
        quantity of the product adn returns the prices of the amount of products
        bought"""
        if self.get_quantity() - quantity < 0:
            raise Exception("Insufficient quantity")
        price_of_purchase = quantity * self.price
        self.set_quantity(self.get_quantity() - quantity)
        return price_of_purchase


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


if __name__ == "__main__":
    main()
