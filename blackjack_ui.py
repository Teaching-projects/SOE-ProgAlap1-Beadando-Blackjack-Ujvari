import cards as CARDS
import json
import os.path

def options():
    print()
    print("Options: ")
    print("1: Hit")
    print("2: Stay")
    print("3: Current result to a json file and exit")
    print()

def getOption():
    option = int(input("Please, choose an option! "))
    print()
    while str(option) not in "123": 
        print("Sorry, but there is no {}.option".format(option))
        option = int(input("Please, choose an option! "))
    return option

def main():
    file_exists = os.path.isfile(r'SOE-ProgAlap1-Beadando-Blackjack-Ujvari\blackjack.log')
    if not file_exists:
       with open(r'SOE-ProgAlap1-Beadando-Blackjack-Ujvari\blackjack.log', 'a+') as log:
           pass
    with open(r'SOE-ProgAlap1-Beadando-Blackjack-Ujvari\blackjack.log', 'r+') as log:
       logs = log.readline()
       if logs == '':
          logs = []
       else:
          logs = logs.replace("'",'"')
          logs = json.loads(logs)
          
       player_cards = []
       dealer_cards = []
    
       while True:

           options()
           option = getOption()

           if option == 3:
               CARDS.save(player_cards,dealer_cards)
               exit()

           else:
               CARDS.getDealerCard(dealer_cards)
               print("Dealer has: {}, the sum of his cards is: {}".format(dealer_cards,CARDS.sumOfTheCards(dealer_cards)))
               if CARDS.ifBusted(dealer_cards):
                   print("Dealer has busted, you win.")
                   print("The sum of your cards is: {}".format(CARDS.sumOfTheCards(player_cards)))
                   logs.append({"result":"win","reason":"Dealer has busted."})
                   log.seek(0)
                   log.write(str(logs))
                   log.truncate()
                   return
               if CARDS.ifBlackJack(dealer_cards):
                   print("Dealer has BlackJack. Dealer won the game! ")
                   print("The sum of your cards was: {}".format(CARDS.sumOfTheCards(player_cards)))
                   logs.append({"result":"lose","reason":"Dealer had BlackJack."})
                   log.seek(0)
                   log.write(str(logs))
                   log.truncate()
                   return

               if option == 1:
                   CARDS.getPlayerCard(player_cards)
                   print("You have: {}, the sum of your cards is: {}".format(player_cards,CARDS.sumOfTheCards(player_cards)))
                   if CARDS.ifBusted(player_cards):
                       print("You have busted. Dealer won the game. The sum of the dealer cards is: {}".format(CARDS.sumOfTheCards(dealer_cards)))
                       logs.append({"result":"lose","reason":"Player has busted."})
                       log.seek(0)
                       log.write(str(logs))
                       log.truncate()
                       return
                   if CARDS.ifBlackJack(player_cards):
                       print("You have BlackJack. You won the game! ")
                       print("The sum of the dealer cards was: {}".format(CARDS.sumOfTheCards(dealer_cards)))
                       logs.append({"result":"win","reason":"Player had BlackJack."})
                       log.seek(0)
                       log.write(str(logs))
                       log.truncate()
                       return

               if option == 2:
                   if CARDS.ifSumOfDealerCardsIsLarger(dealer_cards,player_cards):
                       print("Dealer won this game. The sum of his cards is: {}, yours is: {}".format(CARDS.sumOfTheCards(dealer_cards),CARDS.sumOfTheCards(player_cards)))
                       logs.append({"result":"lose","reason":"Dealer was closer to 21."})
                       log.seek(0)
                       log.write(str(logs))
                       log.truncate()
                       return
                   elif CARDS.ifDrawn(dealer_cards,player_cards):
                       print("Drawn. No winner.")
                       logs.append({"result":"draw","reason":"Both got the same value."})
                       log.seek(0)
                       log.write(str(logs))
                       log.truncate()
                       return
                   else:
                       print("You won this game. The sum of your cards is: {}, his is: {}".format(CARDS.sumOfTheCards(player_cards),CARDS.sumOfTheCards(dealer_cards)))
                       logs.append({"result":"win","reason":"Player was closer to 21."})
                       log.seek(0)
                       log.write(str(logs))
                       log.truncate()
                       return


    