"""
This module is for the abstract class Promotion as well as from it deriving classes instantiating
real promotions, which than can be hooked to Product class instances after being instantiated.
:import ABC: in order to make Promotion class abstract.
"""
from abc import ABC, abstractmethod


class Promotion(ABC):
    """
    Abstract base class to make Promotion class easier to use.
    """
    def __init__(self, name: str):
        self._name = name

    @property
    def name(self) -> str:
        """
        Class own protected _name property.
        :return self._name: Class own protected _name property.:
        """
        return self._name

    @abstractmethod
    def apply_promotion(self, product, quantity: int) -> float:
        """
        This method is called when the promotion is applied to the product,
        :param product: Product Object to be promoted.
        :param quantity: int amount of product to be promoted.
        :return total: The float total promotion cost amount.:
        """

class SecondHalfPrice(Promotion):
    """
    Inheriting from abstract class Promotion.
    creating promotions, where every second product gets 50% off.
    """

    def apply_promotion(self, product, quantity: int) -> float:
        """
        This method is called when the promotion is applied to the product,
        instead of the product's buy method.
        :param product: Product Object to be promoted.
        :param quantity: int Amount of product to be promoted.
        :return total: The float total promotion cost amount.
        """
        total = 0
        total += quantity * product.price
        if quantity % 2 == 0:
            # First Product 100% second 50% = 150% / 2 = 75% = 0.75
            total = total * 0.75
        else:
            # Only every second Product should get promoted,
            # every third gets full price.
            total = total * 0.75 + (product.price * 0.5)

        return total

class ThirdOneFree(Promotion):
    """
    Inheriting from abstract class Promotion.
    Creating promotions, where every third product gets 100% off.
    """

    def apply_promotion(self, product, quantity: int) -> float:
        """
        This method is called when the promotion is applied to the product,
        instead of the product's buy method.
        :param product: Product Object to be promoted.
        :param quantity: int Amount of product to be promoted.
        :return total: The float total promotion cost amount.:
        """
        total = 0
        for amount in range(0, quantity):
            if amount % 3 == 0:
                continue
            total += product.price

        return total

class PercentDiscount(Promotion):
    """
    Inheriting from abstract class Promotion.
    Creating percentage promotion for every product gets n% off.
    """
    def __init__(self, name: str, percent: int):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity: int) -> float:
        """
        This method is called when the promotion is applied to the product,
        instead of the product's buy method.
        :param product: Product Object to be promoted.
        :param quantity: int Amount of product to be promoted.
        :return total: The float total promotion cost amount.:
        """
        total = 0
        # get total order amount cost of given Product
        total += quantity * product.price
        # apply promotion of instantiated percent promotion
        # (i.e. subtract it from the total order amount cost
        total -= total * (self.percent / 100)
        return total
