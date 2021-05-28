#inbuilt functions in list

l=[1,2,3,4,5]
#1.count()
print(l.count(4))  #returns the number of occurence of value in the list

#2.index()
print(l.index(4))  #returns the index value of first appearance of value
print(l.index(4,2)) #index with range


#3.append()
l.append(6) #it does nt return any value just used to add elements to the list
print(l)


#4.extend()
l.extend([7,8,9]) #used for adding multiple elements into the list
print(l)

#5.insert(index,value to be entered)
l.insert(0,10) #it is used to insert a value at a particular index value
print(l)

#6.remove()
l.remove(10) #used to remove the first occurence of the value from the list
print(l)


#7.reverse()
l.reverse() #reverse the elements of the list
print(l)


#8.sort()
l.sort() #the function sorts the value in ascending order
print(l)


#9.pop()
l.pop() #this function removes the last element of the list
print(l)
l.pop(3) #if index value is given then it removes the ite,m at that particular index 
print(l)
