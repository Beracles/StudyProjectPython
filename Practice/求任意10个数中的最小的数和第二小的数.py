alist=[]
n=0
while n<10:
    x=int(input("请输入任意10个整数："))
    alist.append(x)
    n+=1
for i in range(len(alist)):
    for j in range(i+1,len(alist)):
        if alist[j]>alist[i]:
            alist[i],alist[j]=alist[j],alist[i]
print(alist[0],alist[1])
    
