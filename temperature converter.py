temp=float(input('Please enter the temperature'))
ch=input('Choose for conversion: Farhenheit [F]    Celcius [C]')
if ch=='F':
    f=(9*(temp/5))+32
    print(str(temp)+' °C is '+str(f)+' in Farhenheit')
elif ch=='C':
    c=(5/9)*(temp-32)
    print(str(temp)+' °F is '+str(c)+' in Celcius')
else:
    print('Enter a valid choice')
