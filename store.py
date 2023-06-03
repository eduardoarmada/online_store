import products


class Store:
    """Creates a Store with its products"""

    def __init__(self, list_of_products):
        self.list_of_products = list_of_products

    def add_product(self, product):
        self.list_of_products.append(product)

    def remove_product(self, product):
        self.list_of_products.removes(product)

    def get_total_quantity(self):
        """Returns to total quantity of products available in the store"""
        return sum([product.get_quantity() for product in self.list_of_products])

    def get_all_products(self):
        """Return a list of all available(active) products in the store"""
        return [product for product in self.list_of_products if product.is_active()]

    def order(self, shopping_list):
        """Buys the amount of each product specified in the tuples list passed in the argument
        and returns the sum of the costs of all the products bought"""
        return sum([product.buy(quantity) for product, quantity in shopping_list])


def main():
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    ]

    store = Store(product_list)
    products = store.get_all_products()
    print(store.get_total_quantity())
    print(store.order([(products[0], 1), (products[1], 2)]))


if __name__ == "__main__":
    main()
