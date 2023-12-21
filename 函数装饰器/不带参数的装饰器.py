from functools import wraps

def decorator(fun):
    @wraps(fun)#用来使被装饰的函数保留原来的函数名字和注释文档
    def wrapper(n):
        #print("I'm doing something before executing",fun.__name__)
        #fun(n)
        #print("I'm doing something after executing",fun.__name__)
        print("I'm wrapping the function '%s'"%(fun.__name__))
        return fun(n)
    return  wrapper

@decorator#此时在应用一个以单个函数作为参数的包裹函数
def fibonacci(n):
    '''斐波那契数列第n项'''
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
    print("斐波那契数列数列第%d项为%d"%(n,b))

#fibonacci=decorator(fibonacci)#使用@符号为使用装饰器的简短方式
a=fibonacci(20)
print(fibonacci.__name__,fibonacci.__doc__)