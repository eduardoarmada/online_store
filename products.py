class Product:
    """Creates a product object with the name, price, and quantity of it"""

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None
        if self.quantity < 0:
            self.active = False
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

    def set_promotion(self, promotion):
        self.promotion = promotion

    def show(self):
        """Displays the basic information of the product"""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Discount: {self.promotion}")

    def buy(self, quantity):
        """Checks whether the number of products bought is not over the
        available products, if so, raises an exception, and in case all
        matches correctly, it rests the quantity of products bought to the total
        quantity of the product adn returns the prices of the amount of products
        bought"""
        if self.get_quantity() - quantity < 0:
            raise Exception("Insufficient quantity")
        self.set_quantity(self.get_quantity() - quantity)
        if self.promotion is None:
            price_of_purchase = quantity * self.price
            return price_of_purchase
        else:
            return self.promotion.apply_promotion(self, quantity)


class NonStockedProduct(Product):
    def __init__(self, name, price, quantity=0):
        super().__init__(name, price, quantity)

    def buy(self, quantity):
        if self.promotion is None:
            price_of_purchase = quantity * self.price
            return price_of_purchase
        else:
            return self.promotion.apply_promotion(self, quantity)

    def show(self):
        print(f"{self.name}, Price: {self.price}, Discount: {self.promotion}, Quantity: Unlimited stock")


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity):
        if quantity > self.maximum:
            raise Exception("Exceeded maximum quantity!")
        return super().buy(quantity)

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Maximum allowed amount: {self.maximum}, Discount: {self.promotion}")


def main():
    pass


if __name__ == "__main__":
    main()
