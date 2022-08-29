i=int(input("enter any no"))
a=0
rev=0
while i>0:
    a=i%10
    rev=(rev*10+a)
    i=i//10
print(rev,"reverse number")