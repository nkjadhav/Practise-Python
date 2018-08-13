##li=range(10)
##print(li)
##
##
##li=range(1,10)
##print(li)
##
##li=range(1,11,2)
##print(li)


import random

number = random.randrange(1,10)
guesses=1
guess=int(input("Guess between 1 to 10 : "))

for i in range(2):
    
    while guess!=number:
        guesses += 1
        if guess > number:
            print(guess, "is too high")
        elif guess < number:
            print (guess, "is too low")
        guess = int(input("\nGuess again:"))
        break
    print("You took", guesses, "guesses")
    
print("You took max guesses! Correct number is " , number)
