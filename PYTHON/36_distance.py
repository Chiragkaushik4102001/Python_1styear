#distance between two points
from math import *
x1,y1=map(int,input("enter X coordinates :").split(","))
x2,y2=map(int,input("enter Y coordinates :").split(","))
a=pow(x2-x1,2)
b=pow(y2-y1,2)
d=sqrt(a+b)
print("the distance between the points is {}".format("%.2f" %d))
