from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, price):
        pass

class RegularDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price * 0.9  # 10% discount

class VIPDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price * 0.8  # 20% discount

class GoldDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price * 0.7  # 30% discount

class DiscountCalculator:
    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy

    def calculate(self, price):
        return self.strategy.apply_discount(price)

# Example usage
discount = DiscountCalculator(VIPDiscount())
print(discount.calculate(100))  # Output: 80.0

