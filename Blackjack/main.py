import random
import art

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(list_of_cards: list):
    """Calculates the score and detects when the user
    or the computer has blackjack """
    if sum(list_of_cards) > 21 and len(list_of_cards) == 2:
        return 0
    if 11 in list_of_cards and sum(list_of_cards) > 21:
        list_of_cards.remove(11)
        list_of_cards.append(1)
    return sum(list_of_cards)


def compare(score_1, score_2):
    """Compares the computer's score with the user's score
    and determines the winner"""
    result = ""
    if score_1 == score_2:
        result = "It's a draw."
    elif score_1 == 0:
        result = "You lose. The opponent has a Blacklack"
    elif score_2 == 0:
        result = "You win with a Blacjack!"
    elif score_2 > 21:
        result = "You went over 21. You lose."
    elif score_1 > 21:
        result = "You win! The  opponent went over 21."
    elif score_2 > score_1:
        result = "You win!"
    elif score_1 > score_2:
        result = "You lose."
    print(result)


def play_blackjack():
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        new_card = deal_card()
        user_cards.append(new_card)
        computer_cards.append(new_card)

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}")
        print(f"Computer's first card: {computer_cards[0]}")

        if computer_score == 0 or user_score == 0 or user_score > 21:
            is_game_over = True

        draw_new_card = input("Do you want to draw another card? Type 'y' for yes and 'n' for no: \n").lower()
        if draw_new_card == "y":
            user_cards.append(deal_card())
        else:
            is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand is: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    compare(score_1 = computer_score, score_2= user_score)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    print(art.logo)
    play_blackjack()
print("Thank you for playing. Goodbye!")