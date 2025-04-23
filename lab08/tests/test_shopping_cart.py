import pytest
from src.shopping_cart import Product, ShoppingCart

@pytest.fixture
def sample_product():
    return Product(id=1, name="Apple", price=100)

@pytest.fixture
def decimal_product():
    return Product(id=2, name="Milk", price=9.99)

@pytest.fixture
def empty_cart():
    return ShoppingCart()

def test_adding(empty_cart, sample_product):
    empty_cart.add_product(sample_product)
    assert sample_product.id in empty_cart.products.keys()
    assert empty_cart.get_product_count() == 1

def test_adding_decimal_product(empty_cart,decimal_product):
    empty_cart.add_product(decimal_product, quantity=8)
    assert empty_cart.get_product_count() == 8
    assert empty_cart.get_total_price() == 79.92

@pytest.mark.parametrize("quantity", [1, 3, 5, 10])
def test_multiple_adding(empty_cart, sample_product, quantity):
    empty_cart.add_product(sample_product, quantity)
    assert empty_cart.get_product_count() == quantity


