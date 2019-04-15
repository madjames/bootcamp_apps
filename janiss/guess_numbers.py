import random

secret = random.randint(1,10)
#print(secret)
won = False
while won != True:
    number=input("Guess a number between 1 and 10:")
    if int(number) > secret :
        print("Too High")
    elif int(number) < secret :
        print("Too Low")
    else :
        print("You Win!")
        won = True
