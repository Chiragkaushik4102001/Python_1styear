#list comprehension
#for creating a list with just one line of code

a=[i for i in range(1,11) if i%2==0]
print(a)
#syntax== [expression  iteration  condition(optional)]

b=[i**2  for i in range(1,11) ]
print(b)

c={ i for i in range(1,11)}
print(c)


d=[ x for x in range(1,11) if x>5]
print(d)
