a=float(input("输入边长a："))
b=float(input("输入边长b："))
c=float(input("输入边长c："))
if a+b>c and b+c>a and c+a>b:
    if a==b or b==c or c==a:
        if a==b and b==c:
            print("该三角形为等边三角形")
        else:
            print("该三角形为等腰三角形")
    elif a**2+b**2==c**2 or b**2+c**2==a**2 or c**2+a**2==b**2:
        print("该三角形为直角三角形")
    else:
        print("该三角形为一般三角形")
else:
    print("这三边不能组成三角形")
