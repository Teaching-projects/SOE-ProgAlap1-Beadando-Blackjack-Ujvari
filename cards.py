import random

possibleCards = [2,3,4,5,6,7,8,9,10, "J","Q", "K", "A"]

def ifCardIsJQK(card):
    return card == "J" or card == "Q" or card == "K"

def ifCardIsA(card):
    return card == "A"

def sumOfTheCards(cards):
    count_A = 0
    sum = 0
    for card in cards:
        if ifCardIsJQK(card):
            sum += 10
        elif ifCardIsA(card):
            count_A += 1
        else: sum += card

    if count_A != 0:
        for i in range(count_A):
            if sum + 11 <= 21:
                sum += 11
            else: sum += 1

    return sum

def ifBlackJack(cards):
    return sumOfTheCards(cards) == 21

def ifBusted(cards):
    return sumOfTheCards(cards) > 21

def ifDrawn(dealer_cards,player_cards):
    return sumOfTheCards(dealer_cards) == sumOfTheCards(player_cards)

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
    return sumOfTheCards(dealer_cards) > sumOfTheCards(player_cards)
