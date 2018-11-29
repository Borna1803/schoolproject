from random import randint

t = ["Papir", "Skare", "Kamen"]

computer = t[randint(0,2)]


player = False

while player == False:
    player = input("Papir, Skare ili Kamen? ")
    if player == computer:
        print ("Izjednacena runda")
    elif player == "Kamen":
        if computer == "Papir":
            print("Izgubio si!", computer, "pokriva", player,)
        else:
            print("Pobijedio si! ", player, "razbija", computer,)
    elif player == "Papir":
        if computer == "Skare":
            print("Izgubio si!", computer, "rezu", player,)
        else:
            print("Pobijedio si! ", player, "pokriva", computer,)
    elif player == "Skare":
        if computer == "Kamen":
            print("Izgubio si! ", computer, "razbija", player,)
        else:
            print("Pobijedio si! ", player, "rezuO", computer,)
    else:
        print("Nepravilan potez! Provjeri jesi li tocno napisao rijec!")

    player = False
    computer = t[randint(0,2)]
    
