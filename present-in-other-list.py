# Q: Given two arrays, 1,2,3,4,5 and 2,3,1,0,5 find which numbers are not present in the second array.
 
a = [1,2,3,4,5,6]
b = [2,3,1,0,6,7] 
c=[]
i=0
while i<len(a):
    m=a[i]
    if m not in b:
        c.append(m)   
    i=i+1
print(c)