# Blackjack or 21 game

from typing import List
import random

possibleCards = [2,3,4,5,6,7,8,9,10, "J","Q", "K", "A"]


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

    return card == "J" or card == "Q" or card == "K"

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

    return card == "A"



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
    14
    >>> sumOfTheCards(['A',6,'A'])
    18
    >>> sumOfTheCards(['A',6,'A',10])
    18
    >>> sumOfTheCards([10,'A','A'])
    12
    """
    count_A = 0
    sum = 0
    for card in cards:
        if ifCardIsJQK(card):
            sum += 10
        elif ifCardIsA(card):
            count_A += 1
        else: sum += card

    if count_A != 0:
        if sum == 10 and count_A >= 2:
            sum = sum + count_A * 1
        else:
            for i in range(count_A):
                if sum + 11 <= 21:
                    sum += 11
                else: sum += 1

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

    return sumOfTheCards(cards) == 21

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

    return sumOfTheCards(cards) > 21

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
    return sumOfTheCards(dealer_cards) == sumOfTheCards(player_cards)

def ifSumOfDealerCardsIsLarger(dealer_cards:List,player_cards:List) -> bool:
    """It decides whether the sum of the dealer cards are larger than the sum of the
    player cards or not.

    Args:
        dealer_cards (List): The cards of the dealer
        player_cards (List): The cards of the player

    Returns:
        bool: Returns True if the sum of the dealer cards are larger, False otherwise.
    """

    return sumOfTheCards(dealer_cards) > sumOfTheCards(player_cards)

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