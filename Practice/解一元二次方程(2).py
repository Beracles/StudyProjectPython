import math
a=float(input("请输入二次项系数:"))
b=float(input("请输入一次项系数:"))
c=float(input("请输入常数项:"))
d=-b/(2*a)
dt=b**2-4*a*c
if a==0:
    print("a不能为0，不是一元二次方程。")
elif dt<0:
    print("方程无实数解")
elif dt==0:
    print("方程有一个实数解：%d"%d)
else:
    e=math.sqrt(dt)
    x1=(-b+e)/(2*a)
    x2=(-b-e)/(2*a)
    print("方程组有两个实数解：%.2f,%.2f"%(x1,x2))