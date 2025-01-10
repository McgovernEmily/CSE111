# We import randint from the random module. This is how
# our computer opponent will play.
from random import randint

# We create a list of options for the computer.
t = ["Rock", "Paper", "Scissors"]

# Set up the computer to randomize between the list.
computer = t[randint(0,2)]

# We set the player to false, so we can iterate the while loop.
player = False

# Setting counter to 0 to count how many time the user plays.
counter = 0
    
while player == False:

    # Adding one to the counter each time the while loop goes through.
    counter += 1

    # Re-randomizing the computer.
    computer = t[randint(0,2)]

    # Asking player to choose an option.
    player = input("Choose: Rock, Paper or Scissors? ")

    # If player is same as computer it is tied and restarts the 
    # player to choose another option.
    if player == computer:
        print ("Tie!")
        player = False

    # If player choose 'Rock', the computer will randomize and 
    # figure our if it is beaten or not.
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            player = False          
        else:
            print("You win!", player, "defeats", computer)
            

    # If player choose 'Paper', the computer will randomize and 
    # figure our if it is beaten or not.
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cuts", player)
            player = False
        else:
            print("You win!", player, "defeats", computer)
            

    # If player choose 'Scissors', the computer will randomize and 
    # figure our if it is beaten or not.
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!", computer, "smashes", player)
            player = False
        else:
            print("You win!", player, "defeats", computer)

    # If player give something not in the category given to them.
    else:
        print("That's not a valid play. Check your spelling!")

print("Thank you for playing! It took you", counter, "times")



