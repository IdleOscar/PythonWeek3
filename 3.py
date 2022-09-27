import math
x = []

def area(a,b):
    for i in range(3):
        a = int(input("Enter 1st side: "))
        b = int(input("Enter 2nd side: "))
        c = math.sqrt(math.pow(a,2)+math.pow(b,2))
        x.append(c)
    o = x[0]
    v = x[0]

    for i in range (3):
        if o<x[i]:
            o =x[i]
        if v>x[i]:
            v =x[i]
    print("The greatest c: ",o)
    print("The greatest c: ", v)
a = 0
b = 0
area(a,b)
#3.2
s = str(input("Enter the text"))
def asd(s):
    x = []

    for i in range(len(s)):
        x.append(s[i])

    for i in range(len(s)):
        for j in range(len(s)):
            if x[i] < x[j]:
                x[i], x[j] = x[j], x[i]
    j = ""

    for i in range(len(s)):
        j = j + x[i]

    print(j)
asd(s)