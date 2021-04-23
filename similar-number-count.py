# find the similar number
list1=[1,2,3,1,5,6,7,8,8,4,3]
i=0
a=[]
b=[]
while i<len(list1):
    count=0
    j=0
    while j<len(list1):
        if list1[i]==list1[j]:
            b.append(list1[i])
            count=count+1
        j=j+1
    k=0
    while k<1:
        if list1[i] not in a:
            a.append(list1[i])
            print(list1[i],"times",count)
        k=k+1
    i=i+1