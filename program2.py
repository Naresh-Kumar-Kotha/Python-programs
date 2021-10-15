# program to find the largest of three numbers
a=int (input('a:'))
b=int (input('b:'))
c=int (input('c:'))

if a>b and a>c:
    print("Largest number is: ",a)
elif b>c and b>a:
    print("Largest number is: ", b)
else:
    print("Largest number is: ", c)