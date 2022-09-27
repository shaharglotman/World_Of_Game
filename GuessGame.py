from random import randint as random

difficulty = None

#Will generate number between 1 to difficulty
def generate_number():
    global secret_number
    secret_number = random(1, difficulty)

#Will prompt the user a number
def get_guess_from_user():

    number_to_guess = None

    print("Guess a number between 1 to {difficulty}.")

    while not number_to_guess:
        guess = input("My guess: ")

        if not guess.isnumeric():
            print(f"Guess must be a number, try again")
            continue

        if not 1 <= int(guess) <= difficulty:
            print(f"Guess must be between 1 to {difficulty}, try again")
            continue

        number_to_guess = True

    return int(guess)

#Will compare the secret generated number to the one prompted by the get guess
def compare_results(guess, secret_number):
    return guess == secret_number

#Will call the functions above and play the game.
def play(difficulty_level):
    global difficulty
    difficulty = difficulty_level

    generate_number()

    guess = get_guess_from_user()
    success = compare_results(guess, secret_number)
    if success:
        print("you guessed right!")
    else:
        print(f"you guessed wrong!\n"
              f"The answer was {secret_number}")
