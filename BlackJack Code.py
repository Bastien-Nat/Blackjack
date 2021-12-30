print("--------------------------------------------------------------------")
print("-------------------------BlackJack Code ----------------------------")
print("--------------------------------------------------------------------")

import random 
import art 

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    user_cards.append(random.choice(cards))
    user_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))

def calculate_scores(cards):
    score = int()
    if len(cards) == 2 and (11 in cards and 10 in cards):
        score = 0
    elif score > 21 and 11 in cards:
            cards.remove(11)
            cards.append(1)
            score = sum(cards)
    else:
            score = sum(cards)
    return score

def compare():
    user_score = calculate_scores(user_cards)
    computer_score = calculate_scores(computer_cards)
    if user_score == computer_score :
        print("it's a draw")
    elif (user_score == 0 and (user_score < 21 or computer_score > 21)) or (user_score < 21 and computer_score > 21) or (user_score < 21 and user_score > computer_score) :
        print("User Wins")
    elif (computer_score == 0 and (user_score < 21 or user_score > 21)) or (computer_score < 21 and user_score > 21) or (computer_score < 21 and computer_score > user_score) :
        print("Computer Wins")

while True :
    user_cards = []
    computer_cards = []
    play_or_end = input("Do you want to play a game of BlackJack ? Type 'y' o 'n': ")
    if play_or_end == "n" :
        print("Ok bye !")
        break
    elif play_or_end == "y" :
        print(logo) 
        deal_card()
        if calculate_scores(computer_cards) == 0 and calculate_scores(user_cards) == 0:
            print(f"Your final hand : {user_cards}")
            print(f"Computer final's hand : {computer_cards}")
            print("it's a draw")
            continue
        elif calculate_scores(user_cards) == 0:
            print(f"Your final hand : {user_cards}")
            print(f"Computer final's hand : {computer_cards}")
            print("User Wins")
            continue 
        elif calculate_scores(computer_cards) == 0 :
            print(f"Your final hand : {user_cards}")
            print(f"Computer final's hand : {computer_cards}")
            print("Computer Wins")
            continue 
        print(f"Your cards : {user_cards}")
        print(f"Computer's final hand: {computer_cards[0]}")
        while sum(user_cards) < 21 :
            get_or_pass = input("Type 'y' to get another card, type 'n' to pass: ")
            if get_or_pass == "n" :
                print(f"Your final hand : {user_cards}")
                print(f"Computer final's hand : {computer_cards}")
                compare()
                break
            else:
                user_cards.append(random.choice(cards))
                print(f"Your cards: {user_cards}")
                if sum(user_cards) == 21 or sum(user_cards) > 21 :
                    compare()
