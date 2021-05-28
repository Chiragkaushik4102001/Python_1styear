#program to check whether the given number is prime or not by for else 
n=int(input("enter your number:"))

for i in range(2,n):
    if n%i==0:
        print("Not a Prime Number")
        break
else:
    print("Prime Number")
