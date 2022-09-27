from random import randint
from currency_converter import CurrencyConverter # https://sdw.ecb.europa.eu/curConverter.do

guess_top_limit = 101
random_amount = randint(1, guess_top_limit)
difficulty = None

#Will get the current currency rate from USD to ILS
def get_money_interval():
    converter = CurrencyConverter()
    random_amount_in_nis = converter.convert(random_amount, 'USD', 'ILS')

    # return array of minimum accepted answer, right answer and maximum accepted answer
    return [
        int(random_amount_in_nis - (5 - difficulty)),
        int(random_amount_in_nis),
        int(random_amount_in_nis + (5 - difficulty))
    ]


#method to prompt a guess from the user
def get_guess_from_user():
    guess_valid = None

    while not guess_valid:
        guess = input(f"Try to guess the amount of {random_amount} USD in NIS: ")

        if not guess.isnumeric():
            print(f"Guess must be a number, try again")
        else:
            guess_valid = True

    return int(guess)


#Will call the functions above and play the game.
def play(difficulty_level):
    global difficulty
    difficulty = difficulty_level

    guess = get_guess_from_user()
    guess_range = get_money_interval()

    success = guess_range[0] <= guess <= guess_range[2]
    if success:
        print("you guessed right!")
    else:
        print("you guessed wrong!")

    print(f"Answer is {guess_range[1]}\n"
          f"According to your selected difficulty level ({difficulty}), "
          f"accepted answers are between {guess_range[0]} and {guess_range[2]}")