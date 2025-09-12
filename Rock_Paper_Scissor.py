'''

1 for rock
-1 for paper
0 for scissor

'''

import random
computer = random.randint(-1,1)
comp = {1:"r",-1:"p",0:"s"}
you = input("Enter your choice : ")
dict = {"r" : 1 , "p": -1,"s":0}
print(f"Computer Choice is : {computer} : {comp[computer]}")
younum = dict[you]
print(f"Your choice is : {dict[you]} : {you}")

if(computer == younum):
    print("It's a draw")

if(computer == -1 and younum == 0):
    print("You win!")
elif(computer == -1 and younum == 1):
    print("You lose")
elif(computer == 1 and younum == 0):
    print("You lose")
elif(computer == 1 and younum == -1):
    print("You win!")
elif(computer == 0 and younum == 1):
    print("You win!")
elif(computer == 0 and younum == -1):
    print("You lose")
else:
    print("Something went wrong")