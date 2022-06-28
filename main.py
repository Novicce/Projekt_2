"""

projekt_1.py: druhý projekt do Engeto Online Python Akademie


autor: Martin Nováček

email: mnovacek@me.com

discord: Novicce #7276

"""


import random
import time
from tokenize import Number


ODDELOVAC = ("-" * 49)

#generator cisel =====================================

def main():
    total_time = game_counter = all_counter = 0
    x = None
    while x != 'q':  

        while True:  
            number = random.randrange(1234, 9877)
            if len(set(str(number))) == 4:
                break
        print(number)
        # while True:  
        #     number = ()
        #     random.randrange(1234, 9999)
        #     if len(set(str(number))) == 4:
        #         print(number)
        #     break

        start = time.time()
        counter = 0
        num = None
        while str(num) != str(number):
            num = get_num()
            match(num, number)
            counter += 1
        end = time.time()
        
        print(f"Correct, you've guessed the right number in {counter} guesses!")
        print(f"This game took {round((end - start), 2)} seconds")
        
        # Hrat znovu
        again = " "
        while not (again == "Y" or again == "N"):
            again = input("Do you want to play again? (Y/N) ").upper()
        if again == "N":
            print("Thank you for playing! Bye bye.")
            break
        
        print()
        game_counter += 1
        total_time += (end - start)
        all_counter += counter
        
        
def match(num, number):
    bulls = cows = 0
    for i in range(4):
        if str(number)[i] in set(str(num)):
            cows += 1
        if str(number)[i] == str(num)[i]:
            bulls += 1
            cows -= 1
    if bulls == 1:
        print(bulls, "bull")
        print(ODDELOVAC)
    else:
        print(bulls, "bulls")
        print(ODDELOVAC)
    if cows == 1:
        print(cows, "cow" )
        print(ODDELOVAC)
    else:
        print(cows, "cows" )
        print(ODDELOVAC)

#========================================================

print(ODDELOVAC)
print("Hi there!")
print(ODDELOVAC)
print(
    "I've generated a random 4 digit number for you,",
    "Let's play a bulls and cows game.",
    sep="\n"
)
print(ODDELOVAC)

#========================================================

def get_num():
    while True:
        num = input(f'Enter a number: ')
        if len(set(str(num))) == 4 and num.isnumeric():
            return num


main()
print()

