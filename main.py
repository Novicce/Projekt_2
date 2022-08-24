"""

projekt_1.py: druhý projekt do Engeto Online Python Akademie


autor: Martin Nováček

email: mnovacek@me.com

discord: Novicce #7276

"""

import random
import time


SEP = "-" * 49


def intro():
    print("Hi there!")
    print(SEP)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")


def generate_number():
    while True:
        number = str(random.randrange(1000, 9999))
        if len(set(number)) == 4:
            return number


def get_guess():
    while True:
        print(SEP)
        guess = input('Enter a number: ')
        print(SEP)
        if len(set(guess)) == 4 and guess.isnumeric():
            return guess
        print("The number must have 4 unique digits!")
        #print(SEP)


def match(guess, secret_number):
    bulls = cows = 0
    for i in range(len(guess)):
        if guess[i] == secret_number[i]:
            bulls += 1
        elif guess[i] in secret_number:
            cows += 1

    print(">>>", guess)
    print(bulls, end="")
    if bulls == 1:
        print(" bull, ", end="")
    else:
        print(" bulls, ", end="")

    print(cows, end="")
    if cows == 1:
        print(" cow")
    else:
        print(" cows")

    return bulls == len(guess)


def game():
    secret_number = generate_number()
    #print("secret number ", secret_number)
    counter = 0

    while True:
        guess = get_guess()
        counter += 1
        if match(guess, secret_number):
            return counter


def main():
    intro()
    total_time = game_counter = all_counter = 0

    playing = True
    while playing:
        start_time = time.time()
        counter = game()
        end_time = time.time()

        print(SEP)
        print(f"Correct, you've guessed the right number in {counter} guesses!")
        print(f"This game took {round((end_time - start_time), 2)} seconds")
        print(SEP)

        game_counter += 1
        total_time += end_time - start_time
        all_counter += counter

        again = ""
        while not (again == "Y" or again == "N"):
            again = input("Do you want to play again? (Y/N) ").upper()
        if again == "N":
            print("Thank you for playing! Bye bye.")
            playing = False


if __name__ == "__main__":
    main()
