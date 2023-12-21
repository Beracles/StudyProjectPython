a=[[201,77],[202,82],[203,93],[204,87],[205,88],[206,91]]
x=int(input("请输入要查找成绩的学号："))
flag=0
for i in range(len(a)):
    if a[i][0]==x:
        flag=1
        print("这位学生的成绩为：%d"%a[i][1])
if flag==0:
    print("学号不存在")
