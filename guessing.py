import random
n = int(input("Enter a number between 0-9, \n"))
x = random.randint(0,9)
print(x)
if n == x:
    print("Well guessed!")
elif n != x:
    print("Again")
       
