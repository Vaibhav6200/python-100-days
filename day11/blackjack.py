import random
import os


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Take a list of cards and returns the score calculated from the cards"""
    # condition for getting blackjack (0 represents we got a blackjack)
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    #  Inside this function, check for an 11(ace). If the score is already over 21, then remove the 11 and replace it with a 1.
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, Opponent has a blackjack"
    elif user_score == 0:
        return "Win, with a blackjack"
    elif user_score > 21:
        return "You went over, You Lose."
    elif computer_score > 21:
        return "Opponent went over, You Win"
    elif user_score > computer_score:
        return "You Wins"
    else:
        return "You Lose"


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Note: if user or computer gets a blackjack then game ends and
    # If the game has not ended, ask the user if they want to draw another card. If 'yes', then use the deal_card() function to
    # add another card to the user_cards list. If no then the game has ended.
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current_score: {sum(user_cards)}")
        print(f"Computer First Card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_selection = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_selection == 'y':
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
            else:
                is_game_over = True


    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


    print(f"Your Final Hand: {user_cards}, Final Score: {user_score}")
    print(f"Computer Final Hand: {computer_cards}, Final Score: {computer_score}")
    print(compare(user_score=user_score, computer_score=computer_score))



while input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower() == 'y':
    os.system("cls")
    play_game()