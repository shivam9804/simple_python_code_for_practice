#FIZZBUZZ
for i in range(0,51):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 != 0 and i % 5 != 0:
        print(i)
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
   
    
   
