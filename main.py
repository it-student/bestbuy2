"""
This is the main file within this repository.
In here everything else needed will be imported and consumed.
"""
import sys
from store import Store
from products import Product

# setup initial stock of inventory
product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                Product("Google Pixel 7", price=500, quantity=250),
               ]

best_buy = Store(product_list)

def create_order(store: Store) -> None:
    """
    Create an order by asking the user in two steps which product and what quantity to buy.
    All this runs in a loop for many products to be able to be bought.
    If both user inputs are left blank, the loop breaks and the list of tuples (orders)
    containing product (Product) and quantity (int) gets forwarded as argument.
    Prints the total order amount of that buy back to the user.
    calls store.order(orders)
    :param store:
    :return:
    """
    list_all_products(store)
    orders = []
    available_products = store.get_all_products()
    print("When you want to finish your order, just press enter twice.")
    while True:
        chosen_product = None
        product_to_order = input("Which product # do you want? ")
        if product_to_order:
            try:
                if int(product_to_order) in range(1, len(available_products)+1):
                    chosen_product = available_products[int(product_to_order)-1]
                else:
                    print("Out of range! Please enter a valid number! ")
                    continue
            except ValueError as e:
                print("Please enter a valid number!", e)
                continue

        quantity_to_order = input("What amount do you want? ")
        if quantity_to_order:
            try:
                if int(quantity_to_order) > 0:
                    order = tuple((chosen_product, int(quantity_to_order)))
                    orders.append(order)
                    print("Product added to list!")
                else:
                    print("Please enter a valid (positive) amount!")
            except ValueError as ev:
                print("Please enter a valid (positive) amount #!", ev)
        if not product_to_order and not quantity_to_order:
            break
    print(f"********\nOrder made! Total payment: ${store.order(orders)}")

def list_all_products(store: Store) -> None:
    """
    List all products in the store, by fetching the list
    of all available products from the store Object itself.
    :param store: The Store Object conataining available products
    :return None:
    """
    list_of_all_products = store.get_all_products()
    print("------")
    for i, product in enumerate(list_of_all_products, start=1):
        print(f"{i}. ", end="")
        product.show()
    print("------")

def show_total_quantity(store: Store) -> None:
    """
    Show the total amount in the store,
    by fetching the item-count from the store Object itself.
    :param store: the Store Object conataining available products
    as well as the total count of the products.
    :return None:
    """
    total_quantity = store.get_total_quantity()
    print("------")
    print(f"Total of {total_quantity} items in store.")
    print("------")

def close_store(_) -> None:
    """
    Close the store, quit the program
    :param _:
    :return None:
    """
    sys.exit()

def start(store: Store) -> None:
    """
    Show (print) the User the store menu
    :param store: Store Object conataining available products
    :return None:
    """
    menu = """
    Store Menu
    ----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit"""

    available_actions = {'1': list_all_products,
                         '2': show_total_quantity,
                         '3': create_order,
                         '4': close_store}
    while True:
        print(menu)
        choice = input("Please choose a number: ")
        available_actions[choice](store)

if __name__ == '__main__':
    start(best_buy)
