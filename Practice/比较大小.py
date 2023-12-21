a=[49,38,65,97,76,13,27,49]
for i in range(len(a)):
    m=1
    for j in range(i,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print(a)
