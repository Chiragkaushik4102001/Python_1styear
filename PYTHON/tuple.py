#tuple in python

''' tuple is immutable and is enclosed in () '''

a=(1,2,3)
b=()
c=(1)
d=(1,) # creation of tuple with single element
e=1,2,3
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))


x=a+e #updation of tuple
print(x)

y=2*x #printing tuple multiple times
print(y)

z=[1,2,3,4] # in case of list del () can be used to delete a particular element
del(z[2])
print(z)

#del(e)
#print(e) #del() casn be used only to delete a whole tuple

print(a[0:2:1]) # slicing in tuple

print(a[::-1]) # to print reverse of a tuple ,list,string

