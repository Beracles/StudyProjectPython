a=[]
for i in range(10):
    b=[]
    x=int(input("请输入学号%d："%(i+1)))
    y=float(input("请输入成绩："))
    b.append(x)
    b.append(y)
    a.append(b)
for j in range(len(a)):
    print(a[j][0],a[j][1])
            
