##IMPORTS
import random

##VARIABLES
user_input = input("Guess a number between 1 and 100: ")
random_number = random.randint(1,100)

##RUN/UPDATE/LOGIC
if random_number == int(user_input):
    print("You guessed the correct number!")
else:
    print("You guessed: %s but the magic number was: %d" % (user_input,random_number))
