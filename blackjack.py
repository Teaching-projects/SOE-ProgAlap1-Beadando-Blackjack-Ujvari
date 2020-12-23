# Blackjack or 21 game

from typing import List
import random

possibleCards = [2,3,4,5,6,7,8,9,10, "J","Q", "K", "A"]
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

    >>> sumOfTheCards([7,2,3])
    12
    >>> sumOfTheCards([3,10,8])
    21
    >>> sumOfTheCards([10,2,"A"])
    13
    >>> sumOfTheCards([8,"A"])
    19
    >>> sumOfTheCards(["Q","K"])
    20
    >>> sumOfTheCards([3,10,'A'])
    14
    >>> sumOfTheCards([3,'A',10])
    24
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

def ifDrawn(dealer_cards:List,player_cards:List) -> bool:
    """This checks if the sum of the dealer cards and the sum of the player cards 
    are equal or not.

    Args:
        dealer_cards (List): the list of cards which the dealer has
        player_cards (List): the list of caards which the player has

    Returns:
        bool: Returns True if the sum of the dealer cards and the player cards are equal,
        False otherwise.
    """
    if sumOfTheCards(dealer_cards) == sumOfTheCards(player_cards):
        return True
    return False

def ifSumOfDealerCardsIsLarger(dealer_cards:List,player_cards:List) -> bool:
    """It decides whether the sum of the dealer cards are larger than the sum of the
    player cards or not.

    Args:
        dealer_cards (List): The cards of the dealer
        player_cards (List): The cards of the player

    Returns:
        bool: Returns True if the sum of the dealer cards are larger, False otherwise.
    """

    if sumOfTheCards(dealer_cards) > sumOfTheCards(player_cards):
        return True
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
    """This function saves the list of player's cards and the sum of them, and also saves
    the dealer's cards and the sum of them to a json file.

    Args:
        player_cards (List): the list of the player's cards
        dealer_cards (List): the list of the dealer's cards
    """
    import json
    file = open("saved.json", "wt")
    eredmeny = {"player_card": player_cards, "sumofplayercards": sumOfTheCards(player_cards),
    "dealer_cards": dealer_cards, "sumofdealercards": sumOfTheCards(dealer_cards)
    }
    json.dump(eredmeny, file)
    file.close()



def main(dealer_cards:List,player_cards:List):
    """This is the main function which help we can play with. 

    Args:
        dealer_cards (List): list of the dealer's cards
        player_cards (List): list of the player's cards
    """
    while True:

        options()
        option = getOption()

        if option == 1 or option == 2:
            getDealerCard(dealer_cards)
            print("Dealer has: {}, the sum of his cards is: {}".format(dealer_cards,sumOfTheCards(dealer_cards)))
            if ifBusted(dealer_cards):
                print("Dealer has busted, you win.")
                print("The sum of your cards is: {}".format(sumOfTheCards(player_cards)))
                return
            if ifBlackJack(dealer_cards):
                print("Dealer has BlackJack. Dealer won the game! ")
                print("The sum of your cards was: {}".format(sumOfTheCards(player_cards)))
                return

        if option == 1:
            getPlayerCard(player_cards)
            print("You have: {}, the sum of your cards is: {}".format(player_cards,sumOfTheCards(player_cards)))
            if ifBusted(player_cards):
                print("You have busted. Dealer won the game. The sum of the dealer cards is: {}".format(sumOfTheCards(dealer_cards)))
                return
            if ifBlackJack(player_cards):
                print("You have BlackJack. You won the game! ")
                print("The sum of the dealer cards was: {}".format(sumOfTheCards(dealer_cards)))
                return

        if option == 2:
            if ifSumOfDealerCardsIsLarger(dealer_cards,player_cards):
                print("Dealer won this game. The sum of his cards is: {}, yours is: {}".format(sumOfTheCards(dealer_cards),sumOfTheCards(player_cards)))
                return
            elif ifDrawn(dealer_cards,player_cards):
                print("Drawn")
                return
            else:
                print("You won this game. The sum of your cards is: {}, his is: {}".format(sumOfTheCards(player_cards),sumOfTheCards(dealer_cards)))
                return

        if option == 3:
            exit()

        if option == 4:
            save(player_cards,dealer_cards)

        if str(option) not in "1234": print("Sorry, but there is no {}.option".format(option))