#to print the numbers not divisible by both 3 and 5 from 1 to 100
i=1
while i<=100:
    if (i%3!=0 ) and (i%5!=0):
        print(i)
    i+=1
