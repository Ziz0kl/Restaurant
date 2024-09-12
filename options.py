import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
class Options:    
    def display_options(self):
        while True:
            choice = input(f"{'-'*40}\n"
                            "1: Create your own Burger\n"
                           "2: Create your own Pizza \n"
                           f"{'-'*40}\n")
            if choice not in ['1' , '2']:
                print("Your input is incorrect try again")
            else:
                break
        return choice
    
    def continue_options(self):
        while True:
            continue_choice = input(f"{'-'*40}\n"
                            "1: Place another order\n"
                           "2: Your reciept \n"
                           f"{'-'*40}\n")
            if continue_choice not in ['1' , '2']:
                print("Your input is incorrect try again")
            else:
                clear_screen()
                break
        return continue_choice 
