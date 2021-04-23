# palandrom number
name=input("enter string")
sam=list(name)
b=[]
i=1
while i<=len(sam):
    b.append(sam[-i])
    i=i+1
if b==sam:
    print("palandrom number")
else:
    print("not a palandrome")
