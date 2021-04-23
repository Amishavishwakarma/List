# Iss program mei humein agar koi number binary form mei diya gaya hai, toh hum uski decimal form nikalna seekhenge.
# content

a=[]
size=int(input("enter the size of the list"))
i=0
while i<size:
    user=int(input("enter the binary number"))
    a.append(user)
    i=i+1
print(a)
b=[]
d=0
l=len(a)
i=1
while i<=l:
    b.append(a[-i])
    d=d+2**(i-1)*a[-i]
    i=i+1
print(d)
