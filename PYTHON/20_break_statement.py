#break statement
a=10
x=int(input("how many candies you want ? "))
i=1
while i<=x:
    if i>a:
        print("out of stock")
        break
    print("candy")
    i=i+1
print("bye")
