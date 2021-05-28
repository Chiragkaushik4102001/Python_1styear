#functions on strings
a="hello world"
#1. CAPITALIZE()
print(a.capitalize()) #makes the first letter of the string capital

#2.CENTER(width,fillcharacter)
print(a.center(25,"9")) #makes the string of the provided width and fills the extra space with the fill character ,putting the string at the center

#3.Count(string,beginning index,ending index)
print(a.count("o",0,len(a))) #searches for a string in the given string in given range of indexes
print(a.count("e"))


#4.endswith(string,beginning index,ending index)
print(a.endswith("ld",0,len(a))) #check whether the given string ends with the entered string

#5.find(str,beg,end)
print(a.find("o",0,len(a))) #used to find the index no of the first occurence of substring in given string
print(a.find("o"))


#6.index(str,beg,end)
print(a.index("o",0,len(a))) #function same as find
print(a.index("o"))


#7.islower()
print(a.islower()) #returns true if all letters in the string is in lowercase else returns false

#8.isupper()
print(a.isupper()) #returns true if all letters are in uppercase else return false

#9.istitle()
print(a.istitle()) #returns true if every word of the string starts with a capital letter elsew return false
b='hello wOrld'
print(b.istitle()) #it only depends upon the first letter of words not on other letters


#10.len()
print(len(a)) #used to calculate the length of string with spaces included


#11.lower()
d='HELLO WORLD'
print(d.lower()) #used to convert the uppercase string to lowercase

#12.upper()
print(a.upper()) #used to convert the lowercase string to uppercase string


#13.max(string)
print(max(a)) #returns the maximum character in given string according to the ASCII value


#14.min(string)
print(min(a)) #returns the least value of the string
# if the string contain spaces then the least value is given to spaces and the min() will return ' ' .


#15.startswith(str,beg,end)
print(a.startswith('hel',0,len(a))) #it is a boolean function which returns true if the given string starts with the passed substring or else returns false


#16.rfind(str,beg,end)
print(a.rfind('l',0,len(a)))  #this function returns the index value of the last occurence of the entered character in the given string
print(a.rfind('l'))


#17.rindex(srt,beg,end)
print(a.rindex('l',0,len(a)))  #this function also returns the index value of last occurence of entered character
print(a.rindex('l',0,len(a)))

#18.swapcase()
print(a.swapcase())  #this function is used to convert the lowercase letters into uppercase and the uppercase letters into the lowercase


#19.title()
print(a.title())  # this function converts the first letter of every word into uppercase in given string


