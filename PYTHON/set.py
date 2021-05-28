#set concept
a={1,1,2,3,4,5,3}
print(a) #set avoid duplication of data hence a value is printed only once.

b={} # empty brackets will be treated as dictionary
print(type(b))

a.add(7) # add() can be used to add elements to a non empty set
print(a)

s={1,2,3}
t={4,5,6}
s.update(t) # update can be used to put the values of one set into another set
print(s)

d={5,4,6,2,3,1,1}#set always prints sorted data ie ascending order
print(d)

print(len(d)) #prints the length of the set(no of elements in set)

#remove(value/element)
d.remove(5)  #used to remove the entered value from the set
print(d)

#discard()
d.discard(2) # also used to remove a value from set
print(d)


#pop()
print(d.pop()) # it removes the first element of the set and returns its value
print(d)


#clear()
print(a.clear()) # used to clear all elements of the set , hence creates an empty set


#max()
print(max(d)) #returns max value of set


#min()
print(min(d)) #returns min value of set

#sum()
print(sum(d)) #returns the sum of elements of set


