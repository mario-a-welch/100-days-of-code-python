from art import logo
import random

print(logo)

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5


# Function to check if the user guessed the correct answer
def check_answer(guess, answer, attempts):
    """Compares guess to the random computer and returns number of turns remaining"""
    if guess > answer:
        print("Too High")
        return attempts - 1
    elif guess < answer:
        print("Too Low")
        return attempts - 1
    else:
        print(f"That's the number! The answer was: {answer}. You Win!!!")


# Function to check the difficulty
def set_difficulty():
    """Allows user to input difficulty and returns the number of attempts allowed base on their choice"""
    difficulty = input("Choose a difficulty! Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return EASY_ATTEMPTS
    else:
        return HARD_ATTEMPTS


def guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = random.randint(1, 100)
    # print(answer)

    attempts = set_difficulty()

    guess = 0
    while guess != answer:
        if attempts > 1:
            print(f"You have {attempts} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            attempts = check_answer(guess, answer, attempts)

        if attempts == 1:
            print(f"Last chance!!! You have {attempts} attempt left.")
            guess = int(input("Make a guess: "))
            attempts = check_answer(guess, answer, attempts)

        if attempts == 0:
            print(f"You've run out of guesses. You Lose. The correct answer was: {answer}")
            return  # Exits function


guessing_game()
