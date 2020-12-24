import cards as CARDS

def options():
    print("Options: ")
    print("1: Hit")
    print("2: Stay")
    print("3: Exit")
    print("4: Save")

def getOption():
    option = int(input("Please, choose an option! "))
    while str(option) not in "1234": 
        print("Sorry, but there is no {}.option".format(option))
        option = int(input("Please, choose an option! "))
    return option

def main():
    player_cards = []
    dealer_cards = []
    
    while True:

        options()
        option = getOption()

        if option == 1 or option == 2:
            CARDS.getDealerCard(dealer_cards)
            print("Dealer has: {}, the sum of his cards is: {}".format(dealer_cards,CARDS.sumOfTheCards(dealer_cards)))
            if CARDS.ifBusted(dealer_cards):
                print("Dealer has busted, you win.")
                print("The sum of your cards is: {}".format(CARDS.sumOfTheCards(player_cards)))
                return
            if CARDS.ifBlackJack(dealer_cards):
                print("Dealer has BlackJack. Dealer won the game! ")
                print("The sum of your cards was: {}".format(CARDS.sumOfTheCards(player_cards)))
                return

        if option == 1:
            CARDS.getPlayerCard(player_cards)
            print("You have: {}, the sum of your cards is: {}".format(player_cards,CARDS.sumOfTheCards(player_cards)))
            if CARDS.ifBusted(player_cards):
                print("You have busted. Dealer won the game. The sum of the dealer cards is: {}".format(CARDS.sumOfTheCards(dealer_cards)))
                return
            if CARDS.ifBlackJack(player_cards):
                print("You have BlackJack. You won the game! ")
                print("The sum of the dealer cards was: {}".format(CARDS.sumOfTheCards(dealer_cards)))
                return

        if option == 2:
            if CARDS.ifSumOfDealerCardsIsLarger(dealer_cards,player_cards):
                print("Dealer won this game. The sum of his cards is: {}, yours is: {}".format(CARDS.sumOfTheCards(dealer_cards),CARDS.sumOfTheCards(player_cards)))
                return
            elif CARDS.ifDrawn(dealer_cards,player_cards):
                print("Drawn")
                return
            else:
                print("You won this game. The sum of your cards is: {}, his is: {}".format(CARDS.sumOfTheCards(player_cards),CARDS.sumOfTheCards(dealer_cards)))
                return

        if option == 3:
            exit()

        if option == 4:
            CARDS.save(player_cards,dealer_cards)