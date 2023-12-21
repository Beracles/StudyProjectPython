#with open('text.txt','a+') as fp:
#    for i in range(10):
#        print(i,sep='\t',file=fp)

#b,c=map(int,input("b,c=").split(','))
#print(b,c)

#例2.1 用户输入一个3位自然数，计算并输入出其百位，十位和个位上的数字
#s=input("请输入一个三位自然数：")
#print("百位：%c\n十位：%c\n个位：%c"%(s[0],s[1],s[2]))

#s=int(input("请输入一个三位自然数："))
#s1=s
#for i in range(0,3):
#    a=s1//10**(2-i)
#    s1=s1%10**(2-i)
#    print("%d"%a)

#s=int(input("请输入一个三位自然数："))
#n1=s//100
#n2=s%100//10  #n2=s//10%10
#n3=s%10
#print("百位：%d\n十位：%d\n个位：%d"%(n1,n2,n3))

#s=int(input("请输入一个三位自然数："))
#for i in range(0,3):
#    r=s%10
#    s=s//10
#    print(r)

#s=int(input("请输入一个三位自然数："))
#a,b=divmod(s,100)
#b,c=divmod(b,10)
#print(a,b,c)

#例3.1 比较大小
#a,b=map(int,input("Input a,b:").split(','))
#print(a) if a>b else print(b)

#例3.4 将成绩从百分制变换到等级制
#score=int(input("请输入分数："))
#if 90<=score <=100:
#    print("A")
#elif 80<=score<90:
#    print("B")
#elif 70<=score<80:
#    print("C")
#elif 60<=score<70:
#    print("D")
#else:
#    print("E")

#例3.6 输入两个数，求最大公约数和最小公倍数
#m=int(input("m="))
#n=int(input("n="))
#p=n*m
#while m%n!=0:
#    #m,n=n,m%n
#    t=n
#    n=m%n
#    m=t
#print(n,p//n)

#例3.7 计算1+2+...+n的值
#n=int(input("请输入n:"))
#s=0
#for i in range(1,n+1):
#    s+=i
#print(s)

#i=1;s=0
#while i<=n:
#    s+=i
#    i+=1
#print(s)

#for letter in 'abcdefg':
#    if letter=='d':
#        pass
#    else:
#        print(letter,end=',')

#例3.8 找出10`100中的所有素数
#import math
#for i in range(10,101):
#    n=int(math.sqrt(i))
#    for j in range(2,n+2):
#        if i%j==0:
#            break
#    if j==n+1:
#        print(i)

#from math import sqrt
#for i in range(10,100):
#    flag=0
#    for j in range(2,int(sqrt(i))+1):
#        if i%j==0:
#            flag=1
#            break
#    if flag==0:
#        print(i)

#例3.9 解方程x+y+z=200,5x+3y+z=300
#for x in range(1,200):
#    for y in range(1,200-x):
#        z=200-x-y
#        if 5*x+3*y+z==300:
#            print("x=%d,y=%d,z=%d"%(x,y,z))

#例3.10 随机出5个两整数相加题，统计出答题正确的题数和用时多少。
#import time,random,operator
#t0=time.time()
#n=0#正确题数
#print("请计算以下随机出现的五个题：")
#for i in range(0,5):
#    a=random.randint(1,100)
#    b=random.randint(1,100)    
#    c=random.randint(1,2)
#    if c==1:
#        op='+'
#        res=a+b
#    else:
#        op='-'
#        res=a-b
#    ans=int(input("%d%c%d="%(a,op,b)))
#    if ans==res:
#        n+=1
#t1=time.time()
#print("对了%d道题，用时%5.2f秒"%(n,t1-t0))

#import random
##random.seed(2)
#for i in range(0,10):
#    print(random.randint(1,10))


#例3.11 快速判断一个数是否为素数
#n=int(input("n="))
#if n<=5:
#    if n==2 or n==3 or n==5:
#        prime=True
#    else:
#        prime=False
#elif n%2==0:      #大于2的偶数不是素数
#    prime=False
#else:
#    m=n%6
#    if not(m==1 or m==5):
#        prime=False
#    else:
#        prime=True
#        for i in range(3,int(n**0.5)+1,2):
#            if n%i==0:
#                prime=False
#                break
#if prime:
#    print(n,"是素数！")
#else:
#    print(n,"不是素数！")

#例4.1 输出列表中所有非空元素。
#list1=['one','two','','three','four']
#for i,v in enumerate(list1):         #enumerate枚举列表所有元素
#    if v!='':
#        print('list(',i,')=',v)

#for i in list1:
#    if i!='':
#        print('list(',list1.index(i),')=',i)

#for i,v in enumerate(list1):
#    print(i,'\t',v)

#例4.2 列表前移n位
#list1=[1,2,3,4,5,6,7,8,9,10]
#n=int(input("n="))
##list1=list1[n:]+list1[:n]

#for i in range(n):
#    list1.append(list1.pop(0))

#print(list1)

#例4.3 将第一个列表和第二个列表中的所有数据组合成一个新列表
#list1=['A','b','c']
#list2=[1,2,3]

#list3=list1+list2
#list1.extend(list2)
#list4=list1
#print(list3,list4,sep='\n')

#list3=[]
#for i in list1:
#    for j in list2:
#        list3.append([i,j])
#print(list3)


#例4.4 判断今天是今年的第几天
#import time
#curdate=time.localtime()
#year,month,day=curdate[:3]
#day30=[31,28,31,30,31,30,31,31,30,31,30,31]
#if year%400==0 or (year%4==0 and year%100!=0):
#    day30[1]=29
#if month==1:
#    Day=day
#else:
#    Day=sum(day30[:month-1])+day
#print(year,'年',month,'月',day,'日是今年第',Day,'天')

#例4.5 输入20个分数，找出其中的最高分数，平均分数，并对其进行从大到小排序。
#def and_(a,b):    #求两个逻辑值的并
#    return (a and b)

#def isnum(a):     #判断字符是否为数字
#    if a>='0' and a<='9':
#        return True
#    else:
#        return False

#def val(lst):
#    return lst[1]

#import functools
#lst=[]
#for i in range(3):
#    print("第%d个学生："%(i+1))
#    x=input("学号：")
#    y=input("分数：")
#    while x=='' or y=='' or not functools.reduce(and_,map(isnum,x+y)):
#        x=input("学号：")
#        y=input("分数：")
#    lst.append([int(x),int(y)])
#sum=0
#max=lst[0][1]
#for i in range(len(lst)):
#    sum+=lst[i][1]
#    if lst[i][1]>=max:
#        max=lst[i][1]
#        location=i+1
#print("最高分：",max,'\n平均分：%5.2f'%(sum/len(lst)))
#print("最高分的位置为：",location)
#lst.sort(reverse=True,key=val)
#print(lst,sep='\n')

#嵌套列表平铺
#lst=[[1,2,3],[4,5,6],[7,8,9]]

#lst1=[exp for elem in lst for exp in elem]
#print(lst1)
#相当于
#lst1=[]
#for elem in lst:
#    for exp in elem:
#        lst1.append(exp)
#print(lst1)

#元素条件过滤
#lst=[1,-2,3,-4,5,-6,7,-8,9,-10]
#lst1=[i for i in lst if i+2>=0]
#print(lst1)
#print(lst1.index(max(lst1)))

#例4.6 接收一个所有元素值都不相等的整数列表x和一个整数n，
#要求将值为n的元素作为支点，将列表中所有值小于n的元素全
#部放到其前面，所有值大于n的元素全部放到其后面
#一开始想法：输入一个整数列表，由用户决定列表元素个数，
#输入特定的字符（串）结束输入，然后让用户输入n的值，然后比较大小，
#大于n的挪到最后，小于n的插入到最前，然后把原来的值删掉，或者先保存原来的值，
#然后将列表中原来的值删掉，再将保存的原来的值插入进去😂

#lst=[1,-2,3,-4,5,-6,7,-8,9,-10]
#n=0
#lst1=[i for i in lst if i<n]
#lst2=[i for i in lst if i>n]
#lst3=lst1+[n]+lst2
#print(lst3)

#同时遍历多个列表或可迭代对象
#list1=[1,2,3]
#list2=[1,3,4,5]
#list3=[(x,y) for x in list1 for y in list2 if x==y]   #两个列表同时遍历时用一个条件筛选
#list4=[(x,y) for x in list1 if x==1 for y in list2 if x!=y]      #两个列表同时遍历时用两个条件筛选
#print(list3)
#print(list4)

#复杂的条件筛选
#lst=[1,-2,3,-4]
#print([val+2 if val%2==0 else val+1 for val in lst if val>0])

#import math
#lst=[num for num in range(2,20) if 0 not in [num%g for g in range(2,int(math.sqrt(num)+1))]]
#print(lst)

#生成器推导式
#gen=((j+1)*3 for j in range(6))
#tup1=tuple(gen)
#tup2=tuple(gen)
#print(tup1)
#print(tup2)
#gen=((j+1)*3 for j in range(6))
#print(gen)
#print(gen.__next__())#生成器对象的方法
#print(next(gen))#Python内置函数
#for i in gen:
#    print(i,end=' ')
#lst=list(gen)
#print(lst)

#例4.7 将元组中元素大于平均值的数组成新的元组
#tup=1,2,3,4,5,6,7,8,9
#gen=(t for t in tup if t>sum(tup)//len(tup)) #lst=[t for t in tup if t>sum(tup)//len(tup)]
#tup1=tuple(gen)
#print(tup1)

#test浅复制与深复制
#深复制
#lst=[1,2,3,4,5]
#lst1=lst[:]
#lst[1]=6
#print(lst)
#print(lst1)
#浅复制
#lst=[1,2,3,4,5,6,7,8]
#lst1=list(lst)
#lst[1]=6
#print(lst)
#print(lst1)

#lst=[[1,2,3],[4,5,6],[7,8,9]]
#lst1=list(lst)
#lst[1][2]=3
#print(lst)
#print(lst1)

#理解：引用相当于指针，也就是地址，只存在于于非值对象，如列表、元组等，而对于值对象如整数则不存在
#引用的说法，引用(赋值)过去直接就是完全的复制；所以一维列表在复制时（不管是深复制还是浅复制），副本的值
#的改变不影响原列表的值，因为一维列表的元素即为值本身；而对于二维列表，则有深复制和浅复制的区别，
#原因是二维列表的元素是一维列表，一维列表是一个引用，即地址，副本和原列表指向的是同一段数值，所以
#浅复制的时候副本值的改变会影响到原列表的值

#a=int(input("请输入："))
#print("你输入的内容是：",a);

import json
filename='numbers.json'
with open(filename) as file:
    nums=json.load(file)
print(nums)