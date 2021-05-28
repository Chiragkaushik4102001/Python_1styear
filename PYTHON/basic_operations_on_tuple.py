# basic operations on tuple

#1.len()
a=(1,2,3,4,5,6)
print(len(a))

#2.cancatenation(+)
b=(9,8,7,6,5)
c=a+b
print(c)

#3.repetition(*)
d=a*4
print(d)

#4.membership( in / not in) #boolean exp used to check whether elementpresent in sequence or not
print(10 in a)
print(2 not in a)

#5.iterative elements
for i in a:
    print(i) #used for printing the elements of the tuple one by one

#6.max()
print(max(a))

#7.min()
print(min(a))

#8.index()
print(a.index(4))


#9.count()
print(a.count(1))


#10.conversion to tuple
print(tuple("hello"))  #string to tuple
l=[1,2,3,4,5]
print(tuple(l)) #list to tuple





