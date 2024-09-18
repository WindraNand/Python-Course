import sys
import random
from enum import Enum

def play_rps():
  
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

  if player == 1 and computer == 3:
    print("You win!😎")
  elif player == 2 and computer == 1:
    print("You win!😎")
  elif player == 3 and computer == 2:
    print("You win!😎")
  elif player == computer:
    print("Tie!😐")
  else:
    print("Python wins!😋")

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


play_rps()
