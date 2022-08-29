# i=0
# while i<=10:
#     print(i)
#     i+=1

num=int(input("enter a no"))
num2=num
sum=0
while num2>0:
    rem=num2%10
    sum=sum+rem
    num2=int(num2/10)
if num%sum==0:
    print(num,"is harshad no")
else:
    print(num, "is not harshad no")