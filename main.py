from typing import List


class Operator:
    def __init__(self, name: str, prices: dict):
        self.name = name
        self.prices = prices

    def get_price(self, number: str):
        price: float | None = None
        longest = 0
        for phone_prefix, value in self.prices.items():
            if number.startswith(phone_prefix) and len(phone_prefix) > longest:
                longest = len(phone_prefix)
                price = value
        return price


def find_cheapest_operator(number: str, operators: List[Operator]):
    cheapest_price = float('inf')
    cheapest_operator = None
    for operator in operators:
        price = operator.get_price(number)
        if price is not None and price < cheapest_price:
            cheapest_price = price
            cheapest_operator = operator
    return cheapest_operator, cheapest_price
