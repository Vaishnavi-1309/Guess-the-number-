import random

target=random.randint(1,100)

while True:
    userChoice=int(input("Guess the Target or Quit"))
    if(userChoice=="Quit"):
        break

    userChoice=int(userChoice)
    if(userChoice==target):
        print("Success : Correct guess!!")
        break
    elif(userChoice < target):
        print("Your number was too small.Take a bigger Guess")
    else:
        print("Your number was too big.Take a smaller Guess")

print("----GAME OVER----")