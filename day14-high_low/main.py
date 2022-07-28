import art
import random
from game_data import data
from replit import clear


def get_random_data():
    """Gets data from random account"""
    return random.choice(data)


def format_data(account):
    """Format account information into printable format of: name, description, and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


def check_answer(guess, a_followers, b_followers):
    """Compares a followers and b followers and returns follower with highest count"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(art.logo)

    score = 0

    game_should_continue = True
    account_a = get_random_data()
    account_b = get_random_data()

    while game_should_continue:
        account_a = get_random_data()
        account_b = get_random_data()

        while account_a == account_b:
            account_b = get_random_data()

        print(f"Compare A: {format_data(account_a)}")
        print(art.vs)
        print(f"Compare B: {format_data(account_b)}")

        guess = input("Who has more followers? Type 'A' or Type 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        clear()
        print(art.logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            game_should_continue = False
            print(art.game_over)
            print(f"Sorry, that's wrong. Your final score is: {score}")


game()