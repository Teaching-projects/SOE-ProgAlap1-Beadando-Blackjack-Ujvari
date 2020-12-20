# Blackjack or 21 game

import random

possibleCards = [1,2,3,4,5,6,7,8,9,10, "J","Q", "K", "A"]
player_cards = []
dealer_cards = []


def ifCardIsJQK(card):
    if card == "J" or card == "Q" or card == "K":
        return True
    return False

def ifCardIsA(card):
    if card == "A":
        return True
    return False 

def sumOfTheCards(cards):
    sum = 0
    for card in cards:
        if ifCardIsJQK(card):
            sum += 10
        elif ifCardIsA(card):
            if sum + 11 <= 21:
                sum += 11
            else: sum += 1
        else: sum += card
    return sum

def ifBlackJack(cards):
    if sumOfTheCards(cards) == 21:
        return True
    return False

def ifBusted(cards):
    if sumOfTheCards(cards) > 21: 
        return True
    return False

def ifDrawn(dealer_cards,player_cards):
    if sumOfTheCards(dealer_cards) == sumOfTheCards(player_cards):
        return True
    return False

def options():

    print("Press 1: Hit")
    print("Press 2: Stay")
    print("Press 3: Exit")
    print("Press 4: Save")

def getOption():
    option = int(input("What would you like to do? "))
    return option

def getDealerCard(dealer_cards):
    if sumOfTheCards(dealer_cards) < 17 and not ifBusted(dealer_cards): # Soft17
        card = random.choice(possibleCards)
        dealer_cards.append(card)
        return dealer_cards

def getPlayerCard(player_cards):
    if not ifBusted(player_cards):
        card = random.choice(possibleCards)
        player_cards.append(card)
        return player_cards

def save(player_cards,dealer_cards):
    import json
    file = open("saved.json", "wt")
    eredmeny = {"player_card": player_cards, "sumofplayercards": sumOfTheCards(player_cards),
    "dealer_cards": dealer_cards, "sumofdealercards": sumOfTheCards(dealer_cards)
    }
    json.dump(eredmeny, file)
    file.close()

def ifSumOfDealerCardsIsLarger(dealer_cards,player_cards):
    if sumOfTheCards(dealer_cards) > sumOfTheCards(player_cards):
        return True
    return False 


while True:

    options()
    option = getOption()

    if option == 1 or option == 2:
        getDealerCard(dealer_cards)
        print("Dealer has: {}, the sum of his cards is: {}".format(dealer_cards,sumOfTheCards(dealer_cards)))
        if ifBusted(dealer_cards):
            print("Dealer has busted, you win.")
            print("The sum of your cards is: {}".format(sumOfTheCards(player_cards)))
            break
        if ifBlackJack(dealer_cards):
            print("Dealer has BlackJack. Dealer won the game! ")
            print("The sum of your cards was: {}".format(sumOfTheCards(player_cards)))
            break

    if option == 1:
        getPlayerCard(player_cards)
        print("You have: {}, the sum of your cards is: {}".format(player_cards,sumOfTheCards(player_cards)))
        if ifBusted(player_cards):
            print("You have busted. Dealer won the game. The sum of the dealer cards is: {}".format(sumOfTheCards(dealer_cards)))
            break
        if ifBlackJack(player_cards):
            print("You have BlackJack. You won the game! ")
            print("The sum of the dealer cards was: {}".format(sumOfTheCards(dealer_cards)))
            break

    if option == 2:
        if ifSumOfDealerCardsIsLarger(dealer_cards,player_cards):
            print("Dealer won this game. The sum of his cards is: {}, yours is: {}".format(sumOfTheCards(dealer_cards),sumOfTheCards(player_cards)))
            break
        elif ifDrawn(dealer_cards,player_cards):
            print("Drawn")
            break
        else:
            print("You won this game. The sum of your cards is: {}, his is: {}".format(sumOfTheCards(player_cards),sumOfTheCards(dealer_cards)))
            break

    if option == 3:
        exit()

    if option == 4:
        save(player_cards,dealer_cards)

