import math

print("hello world")
x1=float(input("enter the x1: "))
x2=float(input("enter the x2: "))
y1=float(input("enter the y1: "))
y2=float(input("enter the y2: "))

a= x2 - x1
b= y2 - y1

d=math.sqrt(a**2 + b**2)

print("The distance is: ",d)
print("The round of value is: ",round(d,2))
