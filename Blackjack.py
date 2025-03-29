import Art
import random

def clear_screen():
    """Simulates clearing the screen with many blank lines"""
    print("\n" * 50)

    """Clears the screen, if supported
    if os.name == "nt":  # Windows
        os.system("cls")
    elif os.getenv("TERM"):  # Linux/Mac, aber nur wenn TERM gesetzt ist
        os.system("clear")
        """

def deal_card():
    """Draw a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculation_score(cards):
    """Calculates the score of a hand of cards. Blackjack check (ace + 10-card)"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0 # 0 stands for Blackjack

    # Convert ace (11) to 1 if necessary
    score = sum(cards)
    while 11 in cards and score > 21:
        cards[cards.index(11)] = 1
        score = sum(cards)

    return score

def compare(user_score, cp_score):
    """Compares the results of player and computer"""
    if user_score == cp_score:
        return "Draw"
    elif cp_score == 0:
        return "You lose, your opponent has Blackjack!"
    elif user_score == 0:
        return "You win, you have a Blackjack!"
    elif cp_score > 21:
        return "You win, your opponent went over!"
    elif user_score > 21:
        return "You lose, you went over!"
    elif user_score > cp_score:
        return "You win!"
    else:
        return "You lose!"

def play_game():
    """Starts a new game Blackjack"""
    clear_screen()

    print(Art.blackjack)
    user_score = -1
    cp_score = -1
    cp_cards = []
    user_cards = []
    start_game = True

    for _ in range(2):
        cp_cards.append(deal_card())
        user_cards.append(deal_card())

    while start_game:
        user_score = calculation_score(user_cards)
        cp_score = calculation_score(cp_cards)
        print(f"     Your cards: {user_cards} , current score: {user_score}")
        print(f"     Computer's first card: {cp_cards[0]}")

        if user_score == 0 or cp_score == 0 or user_score > 21:
            start_game = False
        elif user_score == 21:
            start_game = False
            print("You have 21, no need for more cards.")
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass:     ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                start_game = False

    while cp_score != 0 and cp_score < 17:
        cp_cards.append(deal_card())
        cp_score = calculation_score(cp_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {cp_cards}, final score: {cp_score}")
    print(compare(user_score, cp_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()

