from main import PhoneOperator


class TestOperator:
    prices = {
        "1": 0.9,
        "268": 5.1,
        "46": 0.17,
        "4620": 0.0,
        "468": 0.15,
        "4631": 0.15,
        "4673": 0.9,
        "46732": 1.1,
    }
    operator = PhoneOperator("Operator", prices)

    def test_get_price_should_return_longest_match_price(self):
        number_1 = "46123456789"
        assert self.operator.get_price(number_1) == self.prices["46"]

        number_2 = "46823456789"
        assert self.operator.get_price(number_2) == self.prices["468"]

        number_3 = "46313456789"
        assert self.operator.get_price(number_3) == self.prices["4631"]

        number_4 = "46731456789"
        assert self.operator.get_price(number_4) == self.prices["4673"]

        number_5 = "46732456789"
        assert self.operator.get_price(number_5) == self.prices["46732"]

    def test_get_price_should_return_none_when_no_telephone_prefix_matched(self):
        wrong_number = "44123456789"
        assert self.operator.get_price(wrong_number) is None
