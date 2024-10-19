import random
import art
from game_data import data

def generate_option():
    option = random.choice(data)
    return option


def display_options(option: dict):
    """Displays the person's name, description and country"""
    return f"{option["name"]}, a {option["description"]}, from {option["country"]}"


def compare_followers(count_followers_1: int, count_followers_2: int):
    max_followers = 0
    if count_followers_1 > count_followers_2:
        max_followers = count_followers_1
    elif count_followers_2 > count_followers_1:
        max_followers = count_followers_2
    return max_followers


def game():
    is_game_over = False
    final_score = 0
    option_b = generate_option()
    print(art.logo)
    while not is_game_over:
        option_a = option_b
        option_b = generate_option()

        print(f"Compare A: {display_options(option_a)}")
        print(art.vs)
        print(f"Against B: {display_options(option_b)}")
        followers_a = option_a["follower_count"]
        followers_b = option_b["follower_count"]
        max_followers = compare_followers(followers_a, followers_b)
        guess = input("Who has more followers? Type 'A' or 'B': \n").upper()
        print("\n" * 20)
        print(art.logo)
        if guess == "A":
            guess = followers_a
        else:
            guess = followers_b

        if max_followers == guess:
            final_score += 1
            print(f"That's right. Your final score: {final_score}")
        else:
            is_game_over = True
    print(f"Sorry, that's wrong. Your final score: {final_score}")

game()





