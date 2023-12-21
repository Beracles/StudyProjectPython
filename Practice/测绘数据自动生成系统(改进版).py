import random
qianshi1=[]
qianshi2=[]
houshi1=[]
houshi2=[]
bihecha1=[]
bihecha2=[]
bihechajunzhi=[]
total=[qianshi1,qianshi2,houshi1,houshi2,bihecha1,bihecha2,bihechajunzhi]
for i in range(5000000):
    zhanshu=random.randrange(50,56,2)
    j=0
    for i in range(zhanshu):
        total[0].append(random.randint(1100,1700))
        total[1].append(qianshi1[j]+random.randint(80,200) or qianshi1[j]-random.randint(80,200))
        a=random.randint(0,zhanshu)
        if (a<(zhanshu/4)):
            total[2].append(qianshi1[j]+random.randint(-300,-100) or qianshi1[j]+random.randint(100,300))
        if ((a>=zhanshu/4)):
            total[2].append(qianshi1[j]+random.randint(-100,100))
        total[3].append(-qianshi1[j]+houshi1[j]+qianshi2[j]+random.randint(-3,3))
        total[4].append(houshi1[j]-qianshi1[j])
        total[5].append(houshi2[j]-qianshi2[j])
        total[6].append(round((bihecha1[j]+bihecha2[j])/2.0,1))
        j=j+1
    bihecha=0
    n=0
    for i in range(zhanshu):
        bihecha=bihecha+bihechajunzhi[n]
        n=n+1
    if (abs(bihecha)<=12*(zhanshu**0.5)):
        break
    if (abs(bihecha)>12*(zhanshu**0.5)):
        qianshi1=[]
        qianshi2=[]
        houshi1=[]
        houshi2=[]
        bihecha1=[]
        bihecha2=[]
        bihechajunzhi=[]
        total=[qianshi1,qianshi2,houshi1,houshi2,bihecha1,bihecha2,bihechajunzhi]
        continue
print("站数一共是",zhanshu,"站")
print("站数           后视          前视          高差          平均高差")
sum_hou=sum_qian=0
for i in range(1,zhanshu+1):
    print("%2d"%i,"           ",houshi1[i-1],"         ",qianshi1[i-1],"         ",bihecha1[i-1],"         ")
    print("              ",houshi2[i-1],"         ",qianshi2[i-1],"         ",bihecha2[i-1],"       ",bihechajunzhi[i-1])
    sum_hou=sum_hou+houshi1[i-1]+houshi2[i-1]
    sum_qian=sum_qian+qianshi1[i-1]+qianshi2[i-1]
    print("")
print("整体闭合差=",bihecha)
print("后视之和=",sum_hou,"前视之和=",sum_qian)
print("单位均为毫米,谢谢使用,作者：发")
            
