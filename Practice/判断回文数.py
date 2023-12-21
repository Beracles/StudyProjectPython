x=int(input("请输入任意整数："))
a=0
b=10**a
c=x//b
while c!=0:
    a+=1
    b=10**a
    c=x//b
print("这个整数为%d位数"%a)
alist=[]
f=0
y=x
for i in range(1,a+1):
    f=y//(10**(a-i))
    alist.append(f)
    y=y-f*(10**(a-i))
print(alist) 
m=1   
for j in range(len(alist)):
    if alist[j]!=alist[a-j-1]:
        break
        m=0
        print("这个数不是回文数")
if m==1:
    print("这个数是回文数")
    
    
