import getpass
#Some definitions here!

def disappear(x):
    print("\n"*x)

def p1coord():
    p1coord = True

def p2coord():
    p2coord = True

def canstart():
    canstart = True

#Print out the player 1 board.

p1_board=[]
for x in range(5):
    p1_board.append(["o"] * 5)
def print_p1board():
    for row in p1_board:
        print (" ".join(row))
print("First player\'s board:")
print_p1board()
disappear(2)

#Print out the player 2 board.
p2_board=[]
for x in range(5):
    p2_board.append(["o"] * 5)
def print_p2board():
    for row in p2_board:
        print (" ".join(row))
print("Second player\'s board:")
print_p2board()
disappear(2)


#Szóval a saját az fut.
#Asks players name.
player1 = input("What's your name? ")
player2 = input("And yours? ")

#Asks for the first player's ship coordinates.
p1coord()
while p1coord:
    try:
        p1_shiprow_p1=int(getpass.getpass(player1 + "\'s shiprow: "))-1
        p1_shipcol_p1=int(getpass.getpass(player1 + "\'s shipcol: "))-1
        while p1_shipcol_p1 > 4 or p1_shipcol_p1 > 4:
            print("Out of board.")
            p1_shiprow_p1=int(getpass.getpass(player1 + "\'s shiprow: "))-1
            p1_shipcol_p1=int(getpass.getpass(player1 + "\'s shipcol: "))-1
        user_ask_if=input("Do you want the row or col to be changed for the second part of your ship? ")
        while user_ask_if != "row" and user_ask_if != "col":
            print("Not accepted.")
            user_ask_if=input("Do you want the row or col to be changed for the second part of your ship? ")
        if user_ask_if == "row":
            p1_shipcol_p2=p1_shipcol_p1
            p1_shiprow_p2=int(getpass.getpass(player1 + "\'s ship\'s second part: "))-1
            while abs(p1_shiprow_p2-p1_shiprow_p1) != 1 or p1_shiprow_p2 > 4:
                print("Nincs mellette.")
                p1_shiprow_p2=int(getpass.getpass(player1 + "\'s ship\'s second part: "))-1
        elif user_ask_if == "col":
            p1_shiprow_p2=p1_shiprow_p1
            p1_shipcol_p2=int(getpass.getpass(player1 + "\'s ship\'s second part: "))-1
            while abs(p1_shipcol_p2-p1_shipcol_p1) !=1 or p1_shipcol_p2 > 4:
                print("Nincs mellette.")
                p1_shipcol_p2=int(getpass.getpass(player1 + "\'s ship\'s second part: "))-1
        p1coord = False
    except ValueError:
        print("That's not a number.")

#Asks for the second player's ship coordinates.
p2coord()
while p2coord:
    try:
        p2_shiprow_p1=int(getpass.getpass(player2 + "\'s shiprow: "))-1
        p2_shipcol_p1=int(getpass.getpass(player2 + "\'s shipcol: "))-1
        while p2_shipcol_p1 > 4 or p2_shipcol_p1 > 4:
            print("Out of board.")
            p2_shiprow_p1=int(getpass.getpass(player2 + "\'s shiprow: "))-1
            p2_shipcol_p1=int(getpass.getpass(player2 + "\'s shipcol: "))-1
        user_ask_if=input("Do you want the row or col to be changed for the second part of your ship? ")
        while user_ask_if != "row" and user_ask_if != "col":
            print("Not accepted.")
            user_ask_if=input("Do you want the row or col to be changed for the second part of your ship? ")
        if user_ask_if == "row":
            p2_shipcol_p2=p2_shipcol_p1
            p2_shiprow_p2=int(getpass.getpass(player2 + "\'s ship\'s second part: "))-1
            while abs(p2_shiprow_p2-p2_shiprow_p1) != 1 or p2_shiprow_p2 > 4:
                print("Nincs mellette.")
                p2_shiprow_p2=int(getpass.getpass(player2 + "\'s ship\'s second part: "))-1
        elif user_ask_if == "col":
            p2_shiprow_p2=p2_shiprow_p1
            p2_shipcol_p2=int(getpass.getpass(player2 + "\'s ship\'s second part: "))-1
            while abs(p2_shipcol_p2-p2_shipcol_p1) !=1 or p2_shipcol_p2 > 4:
                print("Nincs mellette.")
                p2_shipcol_p2=int(getpass.getpass(player2 + "\'s ship\'s second part: "))-1
        p2coord = False
    except ValueError:
        print("That's not a number.")

canstart()

#Starts the game.
while canstart:
    #First player turn!
    print(player2 + "\'s board:")
    print_p2board()
    print(player1 + "\'s shot: ")
    
    #Ask player 1 for coordinates: 
    p1_sor=int(input("Row guess: "))-1
    p1_oszlop=int(input("Col guess: "))-1
    
    #If hit, change the list item to "*", if not, change list item to "X"
    if (p1_sor == p2_shiprow_p1 and p1_oszlop == p2_shipcol_p1) or (p1_sor == p2_shiprow_p2 and p1_oszlop == p2_shipcol_p2):
        if p2_board[p1_sor][p1_oszlop] == "*":
            print("You shot that one already!")
        else:
            p2_board[p1_sor][p1_oszlop] = "*"
            print("Good shot!")
    else:
        if (p1_sor < 0 or p1_sor > 4) or (p1_oszlop < 0 or p1_oszlop > 4):
            print("You missed the entire board!")
        elif p2_board[p1_sor][p1_oszlop] == "X":
            print("You shot that one already!")
        else:
            p2_board[p1_sor][p1_oszlop] = "X"
            print("Missed!")
    print_p2board()
    print("-----------")
    
    #Checks if there are 2 "*" in the player 2's board, if it's true, than player one wins.
    starcount = sum(x.count("*") for x in p2_board)
    if starcount == 2:
        print(player1 + " wins!")
        break
    
    #Second player turn!
    print(player1 + "\'s board:")
    print_p1board()
    print(player2 + "\'s shot: ")
    
    #Asks player 2 for coordinates:
    p2_sor=int(input("Row guess: "))-1
    p2_oszlop=int(input("Col guess: "))-1
    
    # If it hits, change list item to "*", if misses, change list item to "X"
    if (p2_sor == p1_shiprow_p1 and p2_oszlop == p1_shipcol_p1) or (p2_sor == p1_shiprow_p2 and p2_oszlop == p1_shipcol_p2):
        if p1_board[p2_sor][p2_oszlop] == "*":
            print("You shot that one already!")
        else:
            p1_board[p2_sor][p2_oszlop] = "*"
            print("Good shot!")
    else:
        if (p2_sor < 0 or p2_sor > 4) or (p2_oszlop < 0 or p2_oszlop > 4):
            print("You missed the entire board!")
        elif p1_board[p2_sor][p2_oszlop] == "X":
            print("You shot that one already!")
        else:
            p1_board[p2_sor][p2_oszlop] = "X"
            print("Missed!")
    print_p1board()
    print("---------")
    
    #Checks if there are 2 "*" in the player 1's board, if it's true, than player two wins.
    starcount = sum(x.count("*") for x in p1_board)
    if starcount == 2:
        print(player2 + " wins!")
        break
