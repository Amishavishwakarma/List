# Ask user to give integer inputs to make a list. Store only even values given and print the list.
a=[]
i=0
size=int(input("enter the size of the list"))
while i<size:
    user=int(input("enter the number"))
    if user%2==0:
        a.append(user)
    i=i+1
print(a)
