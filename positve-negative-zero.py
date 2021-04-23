Take 20 integer inputs from user and print the following:
number of positive numbers
# number of negative numbers
# number of odd numbers
# number of even numbers
# number of 0s.

a=[]
i=0
while i<5:
    n=int(input("enter the number"))
    a.append(n)
    i=i+1
print(a)
j=0
l=len(a)
while j<l:
    m=a[j]
    print(m)
    if m<0:
        print(m,"is negative number")
    if m>0:
        print(m,"is positive number")
    if m%2==0:
        print(m,"is a even number")
    if m%2!=0:
        print(m,"it is odd number ")
    if m==0:
        print(m,"it is 0s ")
    j=j+1
