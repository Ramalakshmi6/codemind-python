num=int(input())
temp=num*num
sum=0
while(temp>0):
    rem=temp%10
    sum=sum+rem
    temp=temp//10
if(sum==num):
    print("Neon Number")
else:
    print("Not Neon Number")