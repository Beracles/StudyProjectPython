a=[77,42,35,12,101,5]
for i in range(len(a)-1):
    flag = True
    for j in range(len(a)-1-i):
        if a[j] > a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            flag = False
    if flag == True:
        break
print(a)
