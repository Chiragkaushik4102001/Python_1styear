#dictionary

a={"name":"chirag","branch":"CSE","roll no":15}
print(type(a)) #dictionary is a group of (key,values) pairs separated by (,) and enclosed in({}).

#empty dictionary
b={}
print(type(b))

#dictionary can also be created as
d={"a":11,
   "b":12,
   "c":13}
print(d)

#dictionary function
c=dict([('a',1),('b',2)])#this function can be used to create a dictionary 
print(c)
#syntax=dict([(key1,val1),(key2,val2)-----])



#dictionary comprehension
# it is also used for creating a dictionary
q={x:x**2 for x in range(5) }
print(q)
#syntax={ expression  iteration  condition(optional) }


print(q[2]) #in dictionarfy slicing and indexing does nt work,else we use key names to access the elements


