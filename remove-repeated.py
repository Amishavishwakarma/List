# Make a list by taking 10 input from user. Now delete all repeated elements of the list.
# E.g.-
INPUT : [1,2,3,2,1,3,12,12,32]
OUTPUT : [1,2,3,12,32]


a=[]
i=0
size=int(input("enter the size of the  list"))
while i<size:
    user=int(input("enter the number"))
    a.append(user)
    i=i+1
print(a)
mix=a[0]
i=0
while i<len(a):
    mix=a[i]
    i=i+1
print(a)
