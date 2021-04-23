# Write a program to find the product of all elements of a list.
a=[]
i=0
p=1
user=int(input("enter the size of the list"))
while i<user:
    n=int(input("enter the number"))
    a.append(n)
    p=p*n
    i=i+1
print(a)
print(p)