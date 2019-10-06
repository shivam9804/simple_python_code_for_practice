#question number 5

from random import *
print("1.stone")
print("2.scissors")
print("3.paper")
b = int(input("enter your choice"))
print ("you choose:", b)
x = randint(1,3)
print ("computer choose:", x)
if b==1 and x==2 or b==2 and x==3 or b==3 and x==1:
    print ("you win")
elif b==1 and x==3 or b==2 and x==1 or b==3 and x==2:
    print ("you loose")
else:
    print ("draw")
