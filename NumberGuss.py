import random

def number_gussing_game():
    print("Welcome To The Number Gussing Game")
    secreat_number = random.randint(1,100)
    no_of_attempts = 0
    while True:
        try:
            guss = int(input("Enter a number between 1 and 100: "))
            no_of_attempts += 1
            if guss < 1 or guss > 100 :
                print("Guss out of range please enter a number between 1 and 100")
            elif guss > secreat_number:
                print("Too high! Try again.")
            elif guss < secreat_number:
                print("Too low! Try again.")
            else :
                print(f"Congratulations you gussed the number ${no_of_attempts} attempts.")
                break
        except ValueError :
            print("Invalid input! Please Enter a valid input.")
number_gussing_game()