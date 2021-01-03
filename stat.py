import json

with open(r'blackjack.log', 'r') as log:
           logs = log.readline()
           if logs == '':
              logs = []
           else:
              logs = json.loads(logs)

lost = 0
for i in range(len(logs)):
    if logs[i]["result"] == "lose":
        lost += 1

won = 0
for i in range(len(logs)):
    if logs[i]["result"] == "win":
        won += 1

blackjack = 0
for i in range(len(logs)):
    if logs[i]["reason"] == "Player had BlackJack.":
        blackjack += 1

busted = 0
for i in range(len(logs)):
    if logs[i]["reason"] == "Player has busted.":
        busted += 1

drawn = 0
for i in range(len(logs)):
    if logs[i]["reason"] == "Both got the same value.":
        drawn += 1


print(logs)
print("You lost {} times - you busted {} times".format(lost,busted))
print("You won {} times - you had blackjack {} times".format(won,blackjack))
print("You got the same value {} times.".format(drawn))