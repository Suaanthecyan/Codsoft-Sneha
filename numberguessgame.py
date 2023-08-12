#Random Number Guessing Game:

import random
Cnumber=random.randrange(1,101)
userInput=int(input("Entyer your number:"))

if userInput>Cnumber:
    print("Computer Number",Cnumber)
    print("Your guess number is too high")

elif userInput<Cnumber:
    print("Computer Number",Cnumber)
    print("Your guess number is too low")

else:
    print("Computer Number",Cnumber)
    print("Your guess number is equal")