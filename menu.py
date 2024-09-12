class Menu:
    def __init__(self):

        self.burger_menu = {
            "Buns\t": [
                ["White Bun" , 10] , ["Toast Bun" , 10] , ["Brioche Bun" , 20]
            ]
            ,
            "Meats\t": [
                ["Burger Patty" , 50] , ["Smash Patty" , 35] , ["Chicken Breast" , 45] , ["Fish Fillet" , 40]
            ]
            ,
            "Veggies\t": [
                ["Lettuce\t" , 5] , ["Tomatos\t" , 5] , ["Onions\t" , 5] , ["Pickles\t" , 5]  
            ]
            ,
            "Sauces\t": [
                ["Ketchup\t" , 5] , ["Mayonnaise" , 5] , ["Barbeque Sauce" , 10] , ["Ranch Sauce" , 10] , ["Mustard Suace" , 10] , ["Big Tasty Sauce" , 10] , ["Tartar Sauce" , 10]
            ]
            ,
            "Extras\t": [
                ["Mozza Sticks" , 10] , ["Onion Rings" , 10] , ["Jalapenos" , 10] , ["Beef Bacon" , 15] , ["Cheese Bomb" , 20]
            ]
            ,
            "Sides\t": [
                ["French Fries" , 25] , ["Loaded Fries" , 50] , ["Onion Rings" , 30] , ["V Cola\t" , 20] , ["Water\t" , 10]
            ]
        }
        self.pizza_menu = {
            "Sizes\t": [
                ["Small Pizza" , 30] , ["Meduim Pizza" , 50] , ["Large Pizza" , 70] 
            ]
            ,
            "Protiens": [
                ["Ground Beef" , 40] , ["Pepperoni" , 40] , ["Grilled Chicken" , 30] , ["Fried Chicken" , 30] , ["Sasuages" , 30]
            ]
            ,
            "Cheese\t": [
                ["Mozzarella" , 15] , ["Cheddar\t" , 20] , ["Feta Cheese" , 20] , ["Parmasan" , 25]
            ]
            ,
            "Toppings": [
                ["Red Onions" , 5] , ["Tomatos\t" , 5] , ["Peppers\t" , 5] , ["Black Olives" , 5] , ["Pinapples" , 10] , ["Jalapeno" , 10] , ["Beef Bacon" , 15]
            ]
            ,
            "Sauce\t": [
                ["Barbeque Sauce" , 10] , ["Ranch Sauce" , 10] , ["Big Tasty Sauce" , 10] , ["Chili Sauce" , 10] , ["Pesto Sauce" , 10]
            ]

        }
        self.current_category = None


    def get_items(self):
        if self.current_category in self.burger_menu:
            return self.burger_menu[self.current_category]
        elif self.current_category in self.pizza_menu:
            return self.pizza_menu[self.current_category]
        return []
    

    def display_menu(self):
        items = self.get_items()
        print('-' * 41)
        print(f'ID\t{self.current_category}\t\tPrice\t|')
        print('-' * 41)

        for i, item in enumerate(items):
            print(f'{i + 1}:\t{item[0]}\t\t{item[1]} EGP\t|')
        print('-' * 41)
