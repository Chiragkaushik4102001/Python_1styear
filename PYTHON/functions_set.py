#functions on set
a={1,2,3,4,5,6}
b={1,2,3}

#1.issubset()
print(b.issubset(a)) #boolean result,returns true if subset is present in set and false if subset not present in set
#syntax= subset name.issubset(set)

#2.issuperset()
print(a.issuperset(b)) #boolean result,returns true if all elements of subset are present in set else return false
#syntax=set.issuperset(subset name)

#3.union()
print(a.union(b)) #returns a new set with values as union of entered set1 and set2
#syntax=s1.union(s2)

#4.intersection()
print(a.intersection(b)) #returns a new set with values as intersection(common values) from both set1 and set2
#syntax=s1.intersection(s2)

#5.difference()
print(a.difference(b)) #returns a new set with all elements of first set except the common elements of both sets.
#syntax= s1.difference(s2) == returns all values of s1 except the elements common tpo s1 and s2

#6.symmetric_difference()
print(a.symmetric_difference(b)) #returns a new set with all elements of both sets except the common elements to both the sets
#syntax=s1.symmetric_difference(s2)


#7.sorted()
d={6,5,4,3,2,1}
print(sorted(d)) #returns the set in sorted form(ascending order)


