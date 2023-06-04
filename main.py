import products
import store


def main():
    # Creates the products and the store
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    products.NonStockedProduct("Windows License", price=125),
                    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                    ]
    best_buy = store.Store(product_list)

    # Asks the user to input the action that wants to be executed
    users_input = input(""" 
    Store Menu
    ___________
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit\n""")

    while users_input != "4":
        if users_input == "1":
            # Shows the information of each of the products in the store
            for ind, product in enumerate(best_buy.get_all_products()):
                print(f"{ind + 1}. ", end="")
                product.show()
        elif users_input == "2":
            # Prints the total amount of products in the store
            print(f"Total amount of products in store: {best_buy.get_total_quantity()}")
        elif users_input == "3":
            # Creates an order of the products and the desired quantities of this ones
            dict_of_products = {str(ind + 1): product for ind, product in enumerate(
                best_buy.get_all_products())}  # Creates dictionary mapping a number with each product
            for ind, product in enumerate(best_buy.get_all_products()):
                print(f"{ind + 1}. ", end="")
                product.show()
            print("When you want to finish the order, enter empty text.")
            shopping_cart = []
            # Asks the user for the product and the amount of this one that is desired to buy
            product_to_order = input("Which product # do you want to order? ")
            product_quantity = input("What amount do you want? ")
            while product_to_order != "" and product_quantity != "":
                # Adds the product and the desired amount to the shopping cart
                shopping_cart.append((dict_of_products[product_to_order], int(product_quantity)))
                print("Product added to the list!\n")
                product_to_order = input("Which product # do you want to order? ")
                product_quantity = input("What amount do you want? ")
            print("*********")
            try:
                print(best_buy.order(shopping_cart))
            except Exception as e:
                print("An error ocurred regarding to:", e)

        users_input = input(""" 
    Store Menu
    ___________
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit\n""")


if __name__ == "__main__":
    main()
