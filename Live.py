#welcome
def welcome(name):
    print(f"Hello {name} and welcome to the Word of Games(Wog)."
          f"Here you  can find many cool games to play.")

#load_game()
def load_game():
    print("do you want to play again?")
    game = input("Please choose a game to play: 1- Memory Game or 2- Guess Game or 3- Currency Roulette")
    game = game.upper()
    if game == "1":
        print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back ")  # THE PROBLEM IS HERE: IF THE USER INPUT EQUALS "YES", THEN START FROM THE BEGINNING
    elif game == "2":
        print("2. guess game - guess a number and see if you chose like the computer")
    elif game == "3":
        print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
load_game()

#game difficulty
def difficulty():
    difficulty = input("Please choose game difficulty from 1-5: ")
    if difficulty == "1":
        print("The difficulty is Beginner")
    elif difficulty == "2":
        print("The difficulty is Beginner+")
    elif difficulty == "3":
        print("The difficulty is Medium")
    elif difficulty == "4":
        print("The difficulty is Hard!")
    elif difficulty == "4":
        print("The difficulty is Very Hard!")
difficulty()