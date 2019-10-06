# scalene triangle

a = float(input("Enter the fist side of the triangle"))
b = float(input("Enter the second side of the triangle"))
c = float(input("Enter the third side of the triangle"))
if  a != b and b != c and c != a:
    print("Scalene Triangle")
elif a == b and b == c and c==a:
    print("Equilateral Triangle")
else:
    print("Isoceles Triangle")
    
