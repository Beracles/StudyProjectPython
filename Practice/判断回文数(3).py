n=int(input("输入整数："))
sum=0
m=n
while n>0:
    sum=sum*10+n%10
    n=n//10
print(m,end="")
if sum==m:
    print("是回文数")
else:
    print("不是回文数")
