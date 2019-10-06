def fact(num):
    
    factorial = 1
    if num < 0:
       print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
       print("The factorial of 0 is 1")
    else:
       for i in range(1,num + 1):
           factorial = factorial*i
       return factorial

num = int(input("enter the number"))
print("the facorial is :", fact(num))
    
