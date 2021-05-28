#number of vowels and consonants in a string
a=input("enter the string : " )
c=0
d=0
e=0
for i in a:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        c+=1
    
    elif i==" ":
        d+=1
    else:
        e+=1

print("number of vowels is {}".format(c))
print("number of consonants  is {}".format(e))
print("number of white spaces is {}".format(d))

        
