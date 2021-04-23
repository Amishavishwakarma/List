# Ek code likho jo kisi bhi list ke liye yeh output karta hai, ki uss list mei kitne odd numbers hai aur kitne even numbers hai.

elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
count=0
count1=0
while i<len(elements):
    if elements[i]%2==0:
        count=count+1
    if elements[i]%2!=0:
        count1=count1+1
    i=i+1
print("even numbers are",count)
print("odd numbers are",count1)