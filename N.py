i=int(input("enter a no"))
num=1
while i>0:
    num=num*(i%10)
    i=i//10
print(num,"product of digit")