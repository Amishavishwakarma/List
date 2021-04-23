# Q: How to find all pairs in an array of integers whose sum is equal to the given number?
 
number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19] 
m=n
d=0
i=0
s=0
a=[]
while i<len(n):
    j=1
    s=n[i]
    while j<len(m):
        d=m[j]
        if s+d==number:
            print(s,d)

        j=j+1
    i=i+1