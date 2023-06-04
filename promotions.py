from abc import ABC, abstractmethod


class Promotions(ABC):
    def __init__(self, promotion_name):
        self.promotion_name = promotion_name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class PercentageDiscount(Promotions):
    def __init__(self, promotion_name, percentage):
        super().__init__(promotion_name)
        self.percentage = percentage

    def apply_promotion(self, product, quantity):
        return (product.price * (quantity // 2)) * (1 - self.percentage / 100) + product.price * (quantity - (quantity // 2))

    def __str__(self):
        return "Percentage Discount"

class SecondHalfPricePromotion(Promotions):
    def apply_promotion(self, product, quantity):
        return (product.price * (quantity // 2)) / 2 + product.price * (quantity - (quantity // 2))

    def __str__(self):
        return "Second product, half price!"


class Buy2Get1Free(Promotions):
    def apply_promotion(self, product, quantity):
        return product.price * (quantity - (quantity // 3)) * 2

    def __str__(self):
        return "Buy 2, get 1 free!"

