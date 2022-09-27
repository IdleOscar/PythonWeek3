import math
x=int(input("Enter the side of hexagon: "))
def area(x):
    print("Area is: ", math.sqrt(3)*math.pow(x,2)*6/4)
area(x)
#2.2
def rearea(a,b):

        print("The area of rectangle is: ", a*b/2)
for i in range(3):
    a = int(input("Enter first side: "))
    b = int(input("Enter 2nd side: "))
    rearea(a,b)