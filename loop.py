##How do you print even numbers in Python for loop?

import random

##fruits = ["apple", "banana", "cherry"]
##for x in fruits:
  ##print(x)


import random

guess=True

while (guess):
    b = (random.randint(1, 10))
    a = int(input("guess the number"))
    if(a==b) :
        print("you did  the guess the number")
        break
    else:
        print("you did not the guess the number")



