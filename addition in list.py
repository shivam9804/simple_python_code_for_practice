def add():

    list1 = []
    n = int(input("how many numbers do you want to enter"))
    for i in range(n):
        num = int(input("enter numbers"))
        list1.append(num)
    return sum(list1)

print("the sum is:", add())
