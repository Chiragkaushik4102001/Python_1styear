from array import *
a=array('i',[1,2,3,4,5,6,7,8,9])
print(len(a)) #length of array
print(type(a)) #type
print(a.buffer_info()) # give address ,size in form of tuple
a.reverse()  #for reversing values
print(a)
a.reverse()


print(a[0:8])  #for printing specific values


for i in range(len(a)):
    print(a[i])
    # for printing all value one by one


for i in a:
    print(i)


b=array('u',['a','e','i','o','u'])
for i in b:
    print(i)  #character array

#for copying array

c=array(a.typecode,(a for a in a ))  #first and second a refers to array values ,third a is name of array
# typecode says take the type of a
for i in c:
    print(i)


i=0
while i<len(c):
    print(c[i])
    i+=1






