# Report card
marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
]
print("Marks for one year",marks[0])
print("marks for 2nd year",marks[1])
print("marks for 3nd year",marks[2])
i=0
sum=0
l=len(marks[0])
while i<len(marks):
    j=0
    while j<l:
        k=marks[i][j]
        sum=sum+k
        j=j+1
    i=i+1
print(sum)
