"""
This module is a pytest file for testing the products.py files code functionalities.
"""
import pytest
from products import Product
from promotions import SecondHalfPrice, ThirdOneFree, PercentDiscount

def test_creating_products():
    """
    Testing whether product creation works properly, by testing product creation
    with empty name. Should raise a ValueError exception if so.
    """
    # Empty name
    with pytest.raises(ValueError, match="Product Name cannot be empty"):
        Product("", price=1450, quantity=100)


def test_creating_prod_invalid_details():
    """
    Testing whether creating product where details are invalid, crashes.
    Should raise a ValueError exception if so.
    """
    # Negative Price
    with pytest.raises(ValueError, match="Product Price cannot be negative"):
        Product("MacBook Air M2", price=-10, quantity=100)

    # Negative quantity
    with pytest.raises(ValueError, match="Product Quantity cannot be negative"):
        Product("MacBook Air M2", price=1450, quantity=-100)

def test_prod_becomes_inactive():
    """
    Testing whether product becomes inactive once quantity becomes 0.
    """
    test_prod = Product("MacBook Air M2", price=1450, quantity=1)
    test_prod.buy(1)
    assert test_prod.active is False

def test_buy_modifies_quantity():
    """
    Testing whether buy works properly, by testing if qunatity gets modified.
    Should reduce the quantity by the quantity getting bought.
    """
    test_prod = Product("MacBook Air M2", price=1450, quantity=10)
    test_prod.buy(3)
    assert test_prod.quantity == 7

def test_buy_too_much():
    """
    Testing whether buy works properly, by testing if trying to order more than stocked.
    Should raise a ValueError exception.
    """
    test_prod = Product("MacBook Air M2", price=1450, quantity=1)
    with pytest.raises(ValueError,
                       match="Error while making order! Quantity larger than what exists"):
        test_prod.buy(3)

def test_second_half_price_promoted_buy():
    """
    Testing whether second half price is working properly.
    """
    test_prod = Product("MacBook Air M2", price=1450, quantity=10)
    test_second_half_price = SecondHalfPrice("Second Half Price")
    test_prod.promotion = test_second_half_price
    assert test_prod.buy(2) == 2175

def test_third_one_free_promotion():
    """
    Testing whether third one free promotion is working properly.
    """
    test_prod = Product("MacBook Air M2", price=1450, quantity=10)
    test_third_one_free = ThirdOneFree("Third One Free Price")
    test_prod.promotion = test_third_one_free
    assert test_prod.buy(3) == 2900

def test_percent_discount():
    """
    Testing whether percent discount is working properly.
    """
    test_prod = Product("MacBook Air M2", price=1450, quantity=10)
    test_thirty_three_percent_discount = PercentDiscount("Percent Discount", 33)
    test_prod.promotion = test_thirty_three_percent_discount
    assert test_prod.buy(3) == 2914.5
