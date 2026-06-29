"""
This module is mainly for the Product class, which will be instantiated and consumed form here.
"""

class Product:
    """
    Product is a class that will serve to count the total amount of products, as well as
    to enable instantiating Objects as different sellable goods (i.e. MacBook's, Sun-Glasses, et.)
    """
    def __init__(self, name: str, price: float | int, quantity: int):
        if name and len(name) > 0:
            self.name = name
        else:
            raise ValueError("Product Name cannot be empty")
        if price > 0:
            self.price = price
        else:
            raise ValueError("Product Price cannot be negative")
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError("Product Quantity cannot be negative")
        self.active = True

    def get_quantity(self) -> int:
        """
        Returns the quantity of the product Object
        :return self.quantity: An integer representing the quantity of the product.
        """
        return self.quantity

    def set_quantity(self, quantity: int) -> None:
        """
        Sets the quantity of the product Object.
        If quantity is negative, a ValueError will be raised.
        Sets the product Object to inactive if quantity is 0.
        calls self.deactivate() if quantity is 0.
        :param quantity:
        :return None:
        """
        if quantity < 0:
            raise ValueError("Product Quantity cannot be negative")

        self.quantity = quantity
        if self.get_quantity() == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """
        Check whether the Product Object is active or not.
        :return self.active: Boolean value representing whether the Product Object is active or not.
        """
        return self.active

    def activate(self) -> None:
        """
        Activate the Product Object
        :return None:
        """
        self.active = True

    def deactivate(self) -> None:
        """
        Deactivate the Product Object
        :return None:
        """
        self.active = False

    def show(self) -> None:
        """
        Prints a string that represents the Product Object,
        ("MacBook Air M2, Price: 1450, Quantity: 100")
        :return None:
        """
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity: int) -> float:
        """
        Buy a quantity of a Product Object.
        Raises an error if quantity is negative, or quantity is greater than self.quantity.
        :param quantity: The amount to be bought
        :return total: total price of the purchase
        """
        total = 0.0
        if quantity < 0:
            raise ValueError("Product Quantity cannot be negative")
        if quantity <= self.get_quantity():
            total += quantity * self.price
            self.set_quantity((self.get_quantity() - quantity))
        else:
            raise ValueError("Error while making order! Quantity larger than what exists")

        return total
