"""
This module is mainly for the Product class, which will be instantiated and consumed from here.
Also inheriting the Product class, the classes NonStockedProduct and LimitedProduct.
"""
from promotions import Promotion


class Product:
    """
    Product is a class that will serve to count the total amount of products, as well as
    to enable instantiating Objects as different sellable goods (i.e. MacBook's, Sun-Glasses, et.)
    """
    def __init__(self, name: str, price: float | int, quantity: int):
        if name and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Product Name cannot be empty")
        if price > 0:
            self._price = price
        else:
            raise ValueError("Product Price cannot be negative")
        if quantity >= 0:
            self._quantity = quantity
        else:
            raise ValueError("Product Quantity cannot be negative")
        self._active = True
        self._promotion = None

    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price

    @property
    def price(self) -> float:
        """
        Returns the classes own _price of the Product Object
        :return self._price: Price of the Product Object:
        """
        return self._price

    @price.setter
    def price(self, price: float) -> None:
        if price < 0:
            raise ValueError("Product Price cannot be negative")
        self._price = price

    @property
    def name(self) -> str:
        """
        Returns the protected property _name of the Product Object.
        :return self._name: Name of the Product Object
        """
        return self._name

    @property
    def quantity(self) -> int:
        """
        Returns the quantity of the product Object
        :return self.quantity: An integer representing the quantity of the product.
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: int) -> None:
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

        self._quantity = quantity
        if self._quantity == 0:
            self.deactivate()

    @property
    def promotion(self):
        """
        Returns the promotion Object used inside the Product Object.
        :return self.promotion: Promotion object:
        """
        return self._promotion

    @promotion.setter
    def promotion(self, promotion: Promotion) -> None:
        """
        Sets the promotion of the Product Object.
        :param promotion: Promotion object
        """
        if isinstance(promotion, Promotion):
            self._promotion = promotion
        else:
            raise TypeError("Promotion must be a Promotion object")

    @property
    def active(self) -> bool:
        """
        Check whether the Product Object is active or not.
        :return self.active: Boolean value representing whether the Product Object is active or not.
        """
        return self._active

    @active.setter
    def active(self, value: bool) -> None:
        self._active = value

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

    def __str__(self) -> str:
        """
        Prints a string that represents the Product Object,
        ("MacBook Air M2, Price: 1450, Quantity: 100")
        :return None:
        """
        return f"{self._name}, Price: {self._price}, Quantity: {self._quantity}\
{": "+self._promotion.name if self._promotion is not None else ''}"

    def buy(self, quantity: int) -> float:
        """
        Buy a quantity of a Product Object.
        Raises an error if quantity is negative, or quantity is greater than self.quantity.
        :param quantity: The amount to be bought
        :return total: total price of the purchase
        """
        total = 0.0
        if quantity <= 0:
            raise ValueError("Product Quantity cannot be lower than 1")
        if quantity <= self.quantity:
            applicable_promotion = self.promotion
            if applicable_promotion is not None:
                total += applicable_promotion.apply_promotion(self, quantity)
            else:
                total += quantity * self._price
            self.quantity -=  quantity
        else:
            raise ValueError("Error while making order! Quantity larger than what exists")

        return total

class NonStockedProduct(Product):
    """
    NonStockProduct is a class that will serve to count the total amount of products, as well as to
    enable instantiating Objects as different sellable NonStockGoods (i.e. Microsoft-licenses et.)
    """
    def __init__(self, name: str, price: float | int):
        super().__init__(name=name, price=price, quantity=0)

    def __str__(self) -> str:
        return f"{self._name}, Price: {self._price}\
{": "+self.promotion.name if self.promotion is not None else ''}"

    def buy(self, quantity: int) -> float:
        """
         Buy a quantity of a Product Object.
         Raises an error if buying quantity is negative.
        :param quantity: The buying quantity, i.e. amount to be bought.
        :return total: total price of the purchase:
        """
        total = 0.0
        if quantity <= 0:
            raise ValueError("Product Quantity cannot be lower than 1")
        applicable_promotion = self.promotion
        if applicable_promotion is not None:
            total += applicable_promotion.apply_promotion(self, quantity)
        else:
            total += quantity * self._price

        return total

class LimitedProduct(Product):
    """
    LimitedProduct is a class that will serve to count the total amount of products, as well as
    to enable instantiating Objects as different sellable LimitedProducts (i.e. Order Fess, etc.)
    """
    def __init__(self, name: str, price: float | int, quantity: int, maximum: int):
        super().__init__(name=name, price=price, quantity=quantity)
        self.maximum = maximum

    def __str__(self) -> str:
        return f"{self._name}, Price: {self._price}, Quantity: {self.quantity}, \
Maximum: {self.maximum}{": "+self.promotion.name if self.promotion is not None else ''}"

    def buy(self, quantity: int) -> float:
        """
        Buy a quantity of a Product Object.
        Raises an error if quantity is negative, or quantity is greater than self.quantity.
        :param quantity: The amount to be bought
        :return total: total price of the purchase
        """
        total = 0
        if quantity > self.maximum:
            raise ValueError(f"Product Quantity must be between 1 and {self.maximum}")
        total = super().buy(quantity)

        return total
