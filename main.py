import random
overs =int(input("enter the number of overs")) #overs input
compscore = random.randint(0,36) # computer score
print("computer has score=",end="")
print(compscore)
print("your target=",end="")
print(compscore+1)

m=0
x=0

def sum(m): # function for calculating the score of player
    m=compscore
    return m

for i in range(1,overs+1):# loop for number of overs
    for j in range(1,7):  #loop for number of balls
        score=int(input("enter number to bat=")) #player input
        print("computer`s no=",end="")
        compno=random.randint(0,6) #computer number
        print(compno)
        if compno == score:
            print("out")
            break
        else:
             x=x+sum(m)  #calculating the score of player

        if x>compscore:
             break

if x>compscore:
    print("you own the match by",x-compscore-1)
elif x==compscore:
    print("match draw")
else:
    print("computer won the match by",compscore-x-1)



