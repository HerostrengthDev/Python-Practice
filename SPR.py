import random

playing = True
while playing == True :
    wins = 0
    print(
        "Hey! Welcome to my Scissors, Paper, Rock game."
        " How many rounds would you like to play?"
    )
    numGames = int(input())
    totalGames = numGames
    while numGames > 0:
        print("Scissors, Paper or Rock?")
        # Scissors = 1
        # Paper = 2
        # Rock = 3
        options = ["Scissors", "Paper", "Rock"]
        vs = options[random.randint(0, 2)]
        play = input()
        if play == vs:
            print(vs + ", Draw! Go again!")
            numGames += 1
        elif play == "Scissors":
            if vs == "Rock":
                print(f"{vs}, You lose!")
            else:
                print(f"{vs}, You win!")
                wins += 1
        elif play == "Paper":
            if vs == "Scissors":
                print(f"{vs},You lose!")
            else:
                print(f"{vs}, You win!")
                wins += 1
        elif play == "Rock":
            if vs == "Paper":
                print(f"{vs}, You lose!")
            else:
                print(f"{vs}, You win!")
                wins += 1
        numGames -= 1
    if wins > totalGames / 2:
        print(f"You won {wins} out of {totalGames} games, you win!")
    else:
        print(f"You won {wins} out of {totalGames} games, you lose!")
    print("Would you like to play again?")
    x = input()
    if x == "No" :
        playing = False

