#midterm preparation

print(r"chirag\nkaushik")
a="happy\\nkaushik"
print(10*" chirag ")
print(a[::-1])
print(a[-1:5:-1])
print(a[0:22])
a="my"+a[0:]
print(a)
print(len(a))
#a=list(map(int,input("enter the values ").split(" ")))
print(a)
print(a[::-1])
b=[(1,2,30),"chirag",{1,2,3}]
print(type(b[2]))
print(b[::-1])
print(b.extend([1,2]))
print(b)
a=(1,2,3,4,5)
print(a.count(1))
a=10
b=10
c=print(id(a))
d=print(id(b))
print(c is d)
print(id(a) is id(b))
a=11
print(id(a))
print(a//b)
print(a/b)
print(a%b)
print(True +True)
print(type('a'))
a=list(range(1,11))
print(a)
a=22
print(-a)
print(bin(a)[2:])
b=bin(22)
c=bin(11)
print(b+c)
print(hex(0b10110))
#c=input()[0:5]

for i in range(10):
    for j in range(i+1):
        print("*",end=" ")
    print()
print("* "*11)
for i in range(10):
    for j in range(10-i):
        print("*",end=" ")


    print()




