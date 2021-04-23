#find the minimum number in list
a=[1,2,3,5,4]
mini=a[0]
i=0
while i<len(a):
    if a[i]>mini:
        mini=a[i]
    i=i+1
print(mini)