from array import *
a=array('i',[11,22,33,44,55,66,32])
print(a)

print(a.buffer_info())

a.reverse()
print(a)


for i in range (7):
    print(a[i])

print(len(a))
