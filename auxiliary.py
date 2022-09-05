from game_data import data
from art import vs_logo, hi_lo
import random


def clear():
    print('\f\f')


def get_random_account():
    return random.choice(data)


def format_data(account: dict):
    """Formats data taken from the account"""
    name = account['name']
    description = account['description']
    country = account['country']

    return f"{name}, a {description}, from {country}"


def check_answer(guess, a_follower_count, b_follower_count):
    """
    Checks whether your guess is correct or not i.e. have you
    managed to choose account with higher number of followers.
    """
    if a_follower_count > b_follower_count:
        return guess == 'a'
    else:
        # Even if they have the same count as a_follower_count
        # The preference is given to answer 'a'
        return guess == 'b'


def run_game():
    print(f'{hi_lo}\n')
    score = 0
    # Use of flag for while loop
    game_should_continue = True

    # Initialize account_b first to pass it to account_a in
    # while loop
    account_b = data[0]

    while game_should_continue:
        account_a, account_b = account_b, get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}.")
        print(vs_logo)
        print(f"Against B: {format_data(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        clear()
        print(hi_lo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")
