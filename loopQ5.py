i=int(input("enter any no"))
sum=0
while i>0:
    sum=sum+i%10
    i=i//10
    print("sum of digit",sum)

