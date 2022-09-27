import random
import time
import re

time_to_show = 0.5
difficulty = None
system_list = None
user_list = None

#Will generate a list of random numbers between 1 to 101
def generate_sequence():
    global system_list
    system_list = random.sample(range(1, 101), difficulty)

    print(f"A list of random numbers will appear for {time_to_show} seconds.\n"
          f"try to remember as many as you can")
    input("Press Enter to continue...")

    # print array
    for i in system_list:
        print(i, end=' ')

    # wait
    time.sleep(time_to_show)

    # move cursor to line start
    print("\r", end="")

    # hide last line
    for i in system_list:
        print("*", end=' ')
    print("\n")


#Will return a list of numbers
def get_list_from_user():
    global user_list

    while not user_list:
        user_list = input("Type as many number as you remember:\n").replace(",", " ").replace(".", " ")
        if user_list == "":
            print("Type at least one number!")

    # remove double spaces
    user_list = re.sub(' +', ' ', user_list)

    # convert to array
    user_list = user_list.split(" ")
    # convert to array int
    user_list = list(map(int, user_list))


#compare two lists if they are equal
def is_list_equal():
    match_percent = str((len(set(system_list).intersection(set(user_list)))) / len(system_list) * 100) + "%"
    match = all(item in user_list for item in system_list)

    return [match, match_percent];


#Will call the functions above and play the game.
def play(difficulty_level):
    global difficulty
    difficulty = difficulty_level

    generate_sequence()
    get_list_from_user()
    score = is_list_equal()

    if (score[0]):
        print("you guessed right!")
    else:
        print(f"you guessed wrong!\n"
              f"success rate: {score[1]}")