class DiscountCalculator:
    def calculate(self, customer_type, price):
        if customer_type == "regular":
            return price * 0.9  # 10% discount
        elif customer_type == "vip":
            return price * 0.8  # 20% discount
        else:
            return price  # No discount

