a=[]
for i in range(5):
    num=int(input("请输入学生%d的学号："%(i+1)))
    x1=float(input("请输入该学生科目一成绩："))
    x2=float(input("请输入该学生科目二成绩："))
    x3=float(input("请输入该学生科目三成绩："))
    b=[num,x1,x2,x3]
    a.append(b)
c=[]
for j in range(5):
    sum=a[j][1]+a[j][2]+a[j][3]
    c.append(sum)
for k in range(len(c)):
    if c[k]==max(c):
        print("总分最高的学生的学号为：%d"%a[k][0])
        print("科目一：%d"%a[k][1],"\n科目二：%d"%a[k][2],"\n科目三：%d"%a[k][3])
        print("总分：%d"%c[k])
        print("平均分：%f"%(c[k]/3))
