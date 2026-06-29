"""
This module is a pytest file for testing the products.py files code functionalities.
"""
import pytest
from products import Product

def test_creating_products():
    # Empty name
    with pytest.raises(ValueError, match="Product Name cannot be empty"):
        Product("", price=1450, quantity=100)


def test_creating_prod_invalid_details():
    # Negative Price
    with pytest.raises(ValueError, match="Product Price cannot be negative"):
        Product("MacBook Air M2", price=-10, quantity=100)

    # Negative quantity
    with pytest.raises(ValueError, match="Product Quantity cannot be negative"):
        Product("MacBook Air M2", price=1450, quantity=-100)

def test_prod_becomes_inactive():
    test_prod = Product("MacBook Air M2", price=1450, quantity=1)
    test_prod.buy(1)
    assert test_prod.active == False

def test_buy_modifies_quantity():
    test_prod = Product("MacBook Air M2", price=1450, quantity=10)
    test_prod.buy(3)
    assert test_prod.quantity == 7

def test_buy_too_much():
    test_prod = Product("MacBook Air M2", price=1450, quantity=1)
    with pytest.raises(ValueError, match="Error while making order! Quantity larger than what exists"):
        test_prod.buy(3)
