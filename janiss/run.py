# My first Python app
# Cool ! Isn't it?
import os
actions = {"action 2":"practice with Sdx","action 3":"sleep","action 1":"read book"}
while True:
    os.system("cls")
    #print("Python is a programming language\nthat lets yu work quickly\nand integrate systems more effectively\n")
    name = raw_input ("What's your name? ")
    print("Hello, " + name)
    print(actions)
    print("Please choose your action :")
    for name, value in actions.items():
        print(name,value)
    action_rawinput = raw_input("Your choose : ")
    action_input = "action "+str(action_rawinput)
    print("I'll {} later".format(actions.get(action_input))
