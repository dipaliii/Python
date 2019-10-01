print("***************************Hello guess the number***********************************")
import random
n = random.randint(1, 9)
i=0
guess = int(input("Enter an integer from 1 to 9: "))
while i<2:
    if guess < n:
        print("guess is low")
        guess = int(input("Enter an integer from 1 to 9: "))
    elif guess > n:
        print("guess is high")
        guess = int(input("Enter an integer from 1 to 9: "))
    else:
        print("you guessed it!")
        break
    i=i+1
print("max limit is reached")