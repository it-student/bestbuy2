"""
This module is the home of the Store class.
Which will hold Objects of the Product class, add or remove them and
when ordered, updates them.
:import products.Product:
"""
from products import Product

class Store:
    """
    This class will hold Objects of the Product class within product_list,
    add or remove them and when ordered, updates them.
    """
    def __init__(self, products: list[Product]):
        self.product_list = products

    def add_product(self, product: Product) -> None:
        """
        Add a product to the store if it is not already inside product_list.
        If the product already exists, add the quantity on top of
        the quantity of the existing product.
        :param product:
        :return None:
        """
        if isinstance(product, Product):
            if product not in self.product_list:
                self.product_list.append(product)
            else:
                for existing_product in self.product_list:
                    if existing_product.name == product.name:
                        existing_product.set_quantity(
                            existing_product.get_quantity() + product.get_quantity())
        else:
            raise ValueError(f"'{product.name}' is not of Type Product")

    def remove_product(self, product: Product) -> None:
        """
        Remove a product from the store if it is already inside product_list.
        If the product does not exist, raise an Exception.
        :param product:
        :return:
        """
        if isinstance(product, Product):
            if product in self.product_list:
                self.product_list.remove(product)
            else:
                raise Exception(f"'{product.name}' does not exist!")
        else:
            raise ValueError(f"'{product.name}' is not of Type Product")

    def get_total_quantity(self) -> int:
        """
        Get the total quantity of products inside the store
        :return total_quantity: Integer as the total quantity of products
        """
        total_quantity = 0
        for product in self.product_list:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self) -> list[Product]:
        """
        Get all products inside the store which are 'active' and return them.
        :return all_products: A list of all active products
        """
        all_products = []
        for product in self.product_list:
            if product.is_active():
                all_products.append(product)
        return all_products

    def order(self, shopping_list: list[tuple]) -> float:
        """
        Buys the products inside the shopping list and
        returns the total price of the order.
        :param shopping_list: A list of tuples containing Product (Product class) and quantity (int).
        :return total_price: Float representing the total price of the order
        """
        total_price = 0.0
        try:
            for product, quantity in shopping_list:
                if isinstance(product, Product) and int(quantity) > 0:
                    total_price = total_price + product.buy(quantity)
        except TypeError as e:
            print("Type Error", e)
        except ValueError as v:
            print("Value Error", v)
        return total_price
