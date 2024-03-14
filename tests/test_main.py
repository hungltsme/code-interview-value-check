from main import PhoneOperator, find_the_best_operator


class TestMain:
    operator_a_prices = {
        "1": 0.9,
        "268": 5.1,
        "46": 0.17,
        "4620": 0.0,
        "468": 0.15,
        "4631": 0.15,
        "4673": 0.9,
        "46732": 1.1,
    }

    operator_b_prices = {
        "1": 0.92,
        "44": 0.5,
        "46": 0.2,
        "467": 1.0,
        "48": 1.2,
    }
    operator_a = PhoneOperator("Operator A", operator_a_prices)
    operator_b = PhoneOperator("Operator B", operator_b_prices)
    operators = [operator_a, operator_b]

    def test_find_cheapest_operator_should_return_cheapest_operator_and_price(self):
        # Given
        number = "46123456789"

        # When
        cheapest_operator, price = find_the_best_operator(number, self.operators)

        # Expect Operator A is matched
        assert cheapest_operator.name == self.operator_a.name
        assert price == self.operator_a_prices["46"]

        # Increase "46" price of operator A
        self.operator_a_prices["46"] = 0.3

        # When
        cheapest_operator, price = find_the_best_operator(number, self.operators)

        # Expect Operator B is matched
        assert cheapest_operator.name == self.operator_b.name
        assert price == self.operator_b_prices["46"]

    def test_find_cheapest_operator_should_return_none_when_phone_number_does_not_match(self):
        # Given
        wrong_number = "84123456789"

        # When
        cheapest_operator, price = find_the_best_operator(wrong_number, self.operators)

        # Expect Operator is None
        assert cheapest_operator is None

