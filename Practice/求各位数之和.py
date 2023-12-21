x=int(input("请输入任意整数："))
m=1
n=1
k=0
while n!=0:
    k+=1
    m=m*10
    n=x//m
c=0
z=0
y=x
for i in range(k):
    a=10**(k-1)
    y=y-z*a*10
    z=y//a
    c=c+z
    k=k-1
print("这个整数的所有数字之和为：%d"%c)
    
