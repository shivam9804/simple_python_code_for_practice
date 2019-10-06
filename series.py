series = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
count_odd = 0
count_even = 0
for i in series:
    if i % 2 == 0:
        count_even+=1
    else:
        count_odd+=1
print("numbers of even number is:", count_even)
print("numbers of odd numbers is:", count_odd)
