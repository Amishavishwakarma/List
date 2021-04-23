# Write a program to find the sum of all elements of a list.
    a=[]
    i=0
    s=0
    user=int(input("enter the size of the list"))
    while i<user:
        n=int(input("enter the number"))
        a.append(n)
        s=s+n
        i=i+1
    print(a)
    print(s)
    