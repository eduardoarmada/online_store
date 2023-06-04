from abc import ABC, abstractmethod


class Promotions(ABC):
    """Creates a discount on the products, class base for creating different kinds of discounts"""
    def __init__(self, promotion_name):
        self.promotion_name = promotion_name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class PercentageDiscount(Promotions):
    """Creates a discount that consist of the decrease of the total value of the products and the quantities by the
    indicated percentage"""
    def __init__(self, promotion_name, percentage):
        super().__init__(promotion_name)
        self.percentage = percentage

    def apply_promotion(self, product, quantity):
        return product.price * quantity * (1 - self.percentage / 100)

    def __str__(self):
        return "Percentage Discount"


class SecondHalfPricePromotion(Promotions):
    """Creates a discount that consist of each 1 product bought, the next one is 50% off"""
    def apply_promotion(self, product, quantity):
        return (product.price * (quantity // 2)) / 2 + product.price * (quantity - (quantity // 2))

    def __str__(self):
        return "Second product, half price!"


class Buy2Get1Free(Promotions):
    """Creates a discount that consist of each 2 products bought, 1 is free."""
    def apply_promotion(self, product, quantity):
        return product.price * (quantity // 3) * 2 + product.price * quantity % 3

    def __str__(self):
        return "Buy 2, get 1 free!"

