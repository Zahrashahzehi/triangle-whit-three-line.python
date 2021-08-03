a = int(input("enter line : "))
b = int(input("enter line : "))
c = int(input("enter line : "))
if (a+b > c) or (a+c > b) or (b+c > a) : 
    print("yes is a triangle")
elif (a+b == c) or (a+c == b) or (b+c == a) :
    print("yes is a triangle")         
else:
    print("It is not possible")
    