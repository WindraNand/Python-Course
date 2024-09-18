import sys
import random
from enum import Enum

def rps():
    game_count = 0
    player_wins = 0
    computer_wins = 0

    def play_rps():
        nonlocal player_wins
        nonlocal computer_wins
    
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input("\nEnter...\n1 for Rock,\n2 for Paper,\n3 for Scissors:\n\n")

        if playerchoice not in ["1", "2", "3"]:
            print("You must enter 1, 2, or 3.")
            return play_rps()
            
        player = int(playerchoice)

        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print("\nYou chose " + str(RPS(player)).replace('RPS.', '') + ".")
        print("Phyton chose " + str(RPS(computer)).replace('RPS.', '') + ".\n")

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal computer_wins
            
            if player == 1 and computer == 3:
                player_wins += 1
                return "You win!😎"
            elif player == 2 and computer == 1:
                player_wins += 1
                return "You win!😎"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "You win!😎"
            elif player == computer:
                return "Tie!😐"
            else:
                computer_wins += 1
                return "Python wins!😋"

        game_result = decide_winner(player, computer)
        
        print(game_result)
        
        nonlocal game_count
        
        game_count += 1
        
        print("\n Game count: " + str(game_count))
        print("\n Player wins: " + str(player_wins))
        print("\n Computer wins: " + str(computer_wins))

        print("\nPlay again?")
        
        while True:
            playagain = input("\n Y for yes\n Q to quit \n\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break
            
        if playagain.lower() == "y":
            return play_rps()
        else:
            print("thanks for playing! 🙏")
            print("😁😁😁😁😁")
            sys.exit("Bye! 🙋‍♂️\n") 
            
    return play_rps


play = rps()

play()