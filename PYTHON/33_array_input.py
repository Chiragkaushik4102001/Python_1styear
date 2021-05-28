#taking input from the user
from array import *
a=array('i',[])
n=int(input("enter the length of array : "))

for i in range(n):
    x=int(input("enter the next value"))
    a.append(x)  #append is used to add values to the array

print(a)




# to get index number from value entered
#manually
v=int(input("enter the value to be searched :"))
k=0
for i in a:
    if i==v:
        print(k)
        break
    k+=1
    
#by function
print(a.index(v))
