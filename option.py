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
