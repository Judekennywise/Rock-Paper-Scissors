#Rock-paper-scossors game
#game rules:
#Rock beats scissors
#Scissors beats paper
#Paper beats rock
import random
player1 = input("Enter your name: ")
player1 = player1.upper()
player2 = "CPU"
print("Welcome to Rock-Scissors-Paper game {}".format(player1))
possible_options = ["R", "S", "P"]
CPU_guess = random.choice(possible_options)
play_again = "yes"
while play_again == "yes":
    player1_guess = input("Pick an option(R, S, P): ")
    if player1_guess not in possible_options:
        print("ERROR, WRONG OPTION. TRY AGAIN")
        player1_guess = input("Pick another option(R, S, P): ")
    elif CPU_guess == player1_guess:
        player1_guess = input("It's a tie, pick another option: ")
    if player1_guess not in possible_options:
        print("ERROR, WRONG OPTION. TRY AGAIN")
        player1_guess = input("Pick another option(R, S, P): ")
    
    if CPU_guess == "R" and player1_guess == "S":
        print(f"{player1}(Scissors):{player2}(Rock)")
        print(f'{player2}(Wins)')
    if player1_guess == "R" and CPU_guess == "S":
        print(f"{player1}(Rock):{player2}(Scissors)")
        print(f'{player1}(Wins)')
    if CPU_guess == "S" and player1_guess == "P":
        print(f"{player1}(Paper):{player2}(Scissors)")
        print(f'{player2}(Wins)')
    if player1_guess == "S" and CPU_guess == "P":
        print(f"{player1}(Scissors):{player2}(Paper)")
        print(f'{player1}(Wins)')
    if CPU_guess == "P" and player1_guess == "R":
        print(f"{player1}(Paper):{player2}(paper)")
        print(f'{player2}(Wins)')
    if player1_guess == "P" and CPU_guess == "R":
        print(f"{player1}(Paper):{player2}(Rock)")
        print(f'{player1}(Wins)')
    play_again = input("Would you like to play again? (yes / no)")

    
