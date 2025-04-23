import pytest
from src.discount import calculate_discounted_price


class TestDiscount:

    def test_correct_disount(self):
        assert calculate_discounted_price(100,30) == 70

    def test_rounding(self):
        assert calculate_discounted_price(100, 33.33333) == 66.67

    def test_invalid_discount(self):
        with pytest.raises(ValueError):
            calculate_discounted_price(455, "A")
