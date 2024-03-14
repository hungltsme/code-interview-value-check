class PhoneOperator:
    def __init__(self, name: str, prices: dict):
        self.name = name
        self.prices = prices

    def get_price(self, phone_number: str) -> float | None:
        price = None
        longest = 0
        for prefix, value in self.prices.items():
            if phone_number.startswith(prefix) and len(prefix) > longest:
                longest = len(prefix)
                price = value
        return price
