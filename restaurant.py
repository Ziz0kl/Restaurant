from menu import Menu
from options import Options
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Restaurant:
    def __init__(self):
        self.menu = Menu()
        self.option = Options()
        self.my_order = []
        self.bill = 0


    def start_the_order(self):
        self.welcome()
        while True:
            choice = self.option.display_options()
            clear_screen()

            if choice == '1':
                self.burger_order()
            elif choice == '2':
                self.pizza_order()

            if self.option.continue_options() == '2':
                clear_screen()
                self.quit()
                break


    def burger_order(self):
        categories = ["Buns\t" , "Meats\t" , "Veggies\t" , "Sauces\t" , "Extras\t" , "Sides\t"]

        for category in categories:
            self.menu.current_category = category
            self.selected_items()


    def pizza_order(self):
        categories = ["Sizes\t" , "Protiens" , "Cheese\t" , "Toppings" , "Sauce\t" , "Sides\t"]

        for category in categories:
            self.menu.current_category = category
            self.selected_items()


    def selected_items(self):
        self.menu.display_menu()
        while True:
            order = int(input("Please choose what you want to order (by number) (When finished, type 0): "))
            items = self.menu.get_items()
            if 1 <= order <= len(items):
                self.my_order.append(items[order - 1])
            elif order == 0:
                break
            else:
                print("Your input is incorrect, try again.")

        clear_screen()


    def receipt(self):
        print('-' * 42)
        print('ID\tItems\t\t\tPrice\t |')
        print('-' * 42)

        for i, item in enumerate(self.my_order):
            print(f'{i+1}:\t{item[0]}\t\t{item[1]} EGP\t |')
            self.bill += item[1]
        self.bill = round(self.bill * 1.14, 2)  
        print('-' * 42)
        print("\tTax Fee \t\t %14\t |")
        print(f'\tYour Total Bill\t\t{self.bill} EGP |')
        print('-' * 42)


    def welcome(self):
        print('-' * 40)
        print("Welcome to Zeyad's Restaurant")


    def quit(self):
        self.receipt()
        print("Thanks for visiting us!")


m = Restaurant()
m.start_the_order()
