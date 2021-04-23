#assending order
a=[1,3,5,2,8,1]
i=0
while i<len(a):
    j=0
    while j<len(a):
        if a[i]<a[j]:
            tem=a[i]
            a[i]=a[j]
            a[j]=tem
        j=j+1
    i=i+1
print(a)
