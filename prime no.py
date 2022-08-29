num=int(input("enter a no"))
start=0
i=1
while i<=num:
    if num%i==0:
        start+=1
    i+=1
if start==2:
    print("prime no")
else:
    print("not  prime no")
    