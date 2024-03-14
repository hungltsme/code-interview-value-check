from typing import List

from phone_operator import PhoneOperator


def find_the_best_operator(number: str, operators: List[PhoneOperator]):
    min_cost = float('inf')
    operator = None
    for _operator in operators:
        price = _operator.get_price(number)
        if price is not None and price < min_cost:
            min_cost = price
            operator = _operator
    return operator, min_cost


if __name__ == '__main__':
    x, y = find_the_best_operator("10", [])
