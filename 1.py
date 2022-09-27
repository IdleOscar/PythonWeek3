def area(x,b):
    print("Area is: ",x*b)
x=int(input("Enter first value: "))
b=int(input("Enter 2nd value: "))
area(x,b)
#1.2
for i in range(3):
    sum=0
    print("Enter the size of ",i+1 ,"array: ")
    n=int(input())
    x=[]
    for j in range(n):
        print('Enter ', i+1, 'array ', j , 'element: ')
        x.append(int(input()))
    for j in range(n):
        sum+=x[j]
    print("The sum of elements is: ", sum)
    print("The average of elements is: ", sum/2)
