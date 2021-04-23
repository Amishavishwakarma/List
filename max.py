#find the maximum number in list
a=[1,2,3,5,4]
mix=a[0]
i=0
while i<len(a):
    if a[i]>mix:
        mix=a[i]
    i=i+1
print(mix)