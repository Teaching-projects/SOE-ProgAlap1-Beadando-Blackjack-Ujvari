# Blackjack or 21 game

from typing import List
import random

possibleCards = [1,2,3,4,5,6,7,8,9,10, "J","Q", "K", "A"]
player_cards = []
dealer_cards = []


def ifCardIsJQK(card) -> bool:
    """This function decides if the card is J,Q, or K. If yes, returns True, False otherwise.

    Args:
        card (int or str): The card which we want to check if J,Q,K or not

    Returns:
        bool: if card is J,Q,K return True, False otherwise

    >>> ifCardIsJQK(9)
    False
    >>> ifCardIsJQK("J")
    True
    >>> ifCardIsJQK("K")
    True
    >>> ifCardIsJQK("Q")
    True
    """

    if card == "J" or card == "Q" or card == "K":
        return True
    else: return False

def ifCardIsA(card) -> bool:
    """ If the card we get is A, then it returns True, False otherwise.

    Args:
        card (int or str): The card we get

    Returns:
        bool: Returns true if card is A, False otherwise

    >>> ifCardIsA("A")
    True
    >>> ifCardIsA("Q")
    False
    >>> ifCardIsA("10")
    False
    """

    if card == "A":
        return True
    return False 



def sumOfTheCards(cards:List) -> int:
    """This function returns the sum of the cards we have. The value of J,Q,K cards are 10,
    the value of the card A is 1 or 11. If the sum of the cards + 11 <= 21 than it worths
    11, otherwise 1.

    Args:
        cards (List): The cards which we have

    Returns:
        int: Returns the sum of the cards

    >>> sumOfTheCards([1,2,3])
    6
    >>> sumOfTheCards([1,10,8])
    19
    >>> sumOfTheCards([10,2,"A"])
    13
    >>> sumOfTheCards([8,"A"])
    19
    >>> sumOfTheCards(["Q","K"])
    20
    """

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

def ifBlackJack(cards:List) -> bool:
    """If the sum of our cards is 21, namely BlackJack, returns True, False otherwise.

    Args:
        cards (List): The list of cards that we have.

    Returns:
        bool: if BlackJack returns True, False otherwise.

    >>> ifBlackJack(["Q","A"])
    True
    >>> ifBlackJack(["Q",10,"A"])
    True
    >>> ifBlackJack(["K",7,"A"])
    False
    >>> ifBlackJack([10,7,4])
    True
    >>> ifBlackJack([2,3,5])
    False
    """

    if sumOfTheCards(cards) == 21:
        return True
    return False

def ifBusted(cards:List) -> bool:
    """If the values of our cards are more than 21, it means that we are busted,
    the game is over. If more than 21, it returns True, False otherwise.

    Args:
        cards (List): The list of cards which we have.
    Returns:
        bool: Returns True if busted, False otherwise

    >>> ifBusted([10,8,4])
    True
    >>> ifBusted([9,9,8])
    True
    >>> ifBusted([10,"Q"])
    False
    >>> ifBusted(["K", "Q"])
    False
    >>> ifBusted(["K", 5, "A"])
    False
    """

    if sumOfTheCards(cards) > 21: return True
    return False

def options() -> None:
    """ This function shows to the player what options she/he has.
    """

    print("Press 1: Hit")
    print("Press 2: Stay")
    print("Press 3: Exit")
    print("Press 4: Save")

def getOption() -> int:
    """Ask the player which option he wants to choose.

    Returns:
        int: returns an int as an option
    """
    
    option = int(input("What would you like to do? "))
    return option

def getDealerCard(dealer_cards:List) -> List:
    """Dealer get a new card if he is not busted already and if he hasn't reached the value 17 yet.
    It is called the Soft 17.

    Args:
        dealer_cards (List): The list of cards the dealer already has.

    Returns:
        List: Returns the new list of the dealer cards with the new card in it.
    """

    if sumOfTheCards(dealer_cards) < 17 and not ifBusted(dealer_cards): # Soft17
        card = random.choice(possibleCards)
        dealer_cards.append(card)
        return dealer_cards

def getPlayerCard(player_cards:List) -> List:
    """ Player get a new card if he is not already busted. 

    Args:
        player_cards (List): The list of the player cards which he already has.

    Returns:
        List: Returns the new list of player cards.
    """

    if not ifBusted(player_cards):
        card = random.choice(possibleCards)
        player_cards.append(card)
        return player_cards


def save(player_cards:List,dealer_cards:List):
    import json
    file = open("saved.txt", "wt")
    json.dump(player_cards, file)
    json.dump(dealer_cards, file)
    file.close()

"""
while True:

    getDealerCard(dealer_cards)
    print("Dealer has: {}, the sum of his cards is: {}".format(dealer_cards,sumOfTheCards(dealer_cards)))
    if ifBusted(dealer_cards):
        print("Dealer has busted, you win.")
        break
    if ifBlackJack(dealer_cards):
        print("Dealer has BlackJack. Dealer won the game! ")
        break

    options()
    option = getOption()

    if option == 1:
        getPlayerCard(player_cards)
        print("You have: {}, the sum of your cards is: {}".format(player_cards,sumOfTheCards(player_cards)))
        if ifBusted(player_cards):
            print("You have busted. Dealer won the game. ")
            break
        if ifBlackJack(player_cards):
            print("You have BlackJack. You won the game! ")
            break
    if option == 2:
        if sumOfTheCards(dealer_cards) > sumOfTheCards(player_cards):
            print("Dealer won this game. The sum of his cards is: {}, yours is: {}".format(sumOfTheCards(dealer_cards),sumOfTheCards(player_cards)))
            break
        elif sumOfTheCards(dealer_cards) == sumOfTheCards(player_cards):
            print("Drawn")
            break
        else:
            print("You won this game. The sum of your cards is: {}, his is: {}".format(sumOfTheCards(player_cards),sumOfTheCards(dealer_cards)))
            break    
    if option == 3:
        exit()
    if option == 4:
        save(player_cards,dealer_cards)
    else: print("No option like that")
"""