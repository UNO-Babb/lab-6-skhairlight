#DiceRoll.py
#Name: Salsabiel Khair Allah
#Date: Oct.5
#Assignment: Lab 6
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  for i in range(10000):
    die1 = random.randit(1, 6)
    die2 = random.randit(1, 6)
    total = die1+ die2
    rolls[total - 1] += 1  
  #find the sum total of the two dice
  
  #print statictics for dice rolls
  print("Total\tCount\tPercentage")
  for i in range(2,13):
    count = rolls[i - 1]
    percent = (count / 10000) * 100
    print(f"{i}\t{count}\t{percent:.2f}%")


if __name__ == '__main__':
  main()
