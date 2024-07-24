#Names: Zavian M, Emma S, Arjun, Aayaan, Annie T

import random
import pandas as pd
import turtle

# Load the CSV into a DataFrame
wordleData = pd.read_csv('words.csv')

# Generate a random integer within the range of the number of rows in the DataFrame
num = random.randint(0, len(wordleData) - 1)

# Print the random index
#print("Random Index:", num)

# Retrieve and print the word at the random index
wrong=0
word = (wordleData.iloc[num, 0])
#print(word)
prints = ""
win = False
for i in range(5):
  wrong=0
  userGuess = input("Please enter a 5 letter word: ")
  if (len(userGuess))!=5:
    i-=1
    userGuess = input("That is not 5 letters, please enter a 5 letter word: ")
  if userGuess == word:
    print("Yay, you got it in", (i + 1), "guesses!")
    print(prints)
    win = True
    break
  else:
    for i in range(5):
      if (word[i] == userGuess[i]):
        prints += ("|" + word[i])
      else:
        prints += ("|_")
      if (userGuess[i]) in word and (userGuess[i]!=word[i]):
        print(userGuess[i] + " is in the word, but it's not in  box", (i+1))
      elif userGuess[i] not in word:
        wrong+=1
        
      if wrong==5:
        print("None of those letters are right. Try again!")
    prints+=("|\n")
    print(prints)
if win == False:
  print("Nice try, but the word was "  + word)


#Keep going!
#You got this!!!
#YOUR A BEAST!!!
#Good job!!
#
#]]]

