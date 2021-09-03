#Student: Antoinette Afieba Cudjoe
#-----------------

import random

#get random number between 10 and 90
random_number = random.randint(10, 90)

#continue taking guesses until player guess matches random_number
while True:
    #prompt user for input
    print("Guess the number: ")

    #read and store user input 
    userGuessed = int(input(">> "))

    #congratulate player if their guess match random number 
    if userGuessed == random_number:
        print("Congrats, you guessed the correct number!!")
        break

    #otherwise the user has guessed higher or lower  number than random number 
    elif userGuessed > random_number:
        print("Number is too large")
    elif userGuessed < random_number:
        print("Number is too small")
    
