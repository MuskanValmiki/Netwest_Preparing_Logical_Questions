# find the max number.

list=[23,12,54,68,98,25]
i=0
max=0
while i<len(list):
    if max<list[i]:
        max=list[i]
    i+=1
print(max)