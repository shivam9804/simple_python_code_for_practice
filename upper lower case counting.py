a = input("Enter a string") 
count1=0
count2=0
for i in a:
    if (i.isupper()):
        count1=count1+1
    elif (i.islower()):
        count2=count2+1
print("The number of uppercase character is :", count1)
print("The number of lower case character is :", count2)

    
