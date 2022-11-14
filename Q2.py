# Stock price

list=list(map(int,input().split()))
l=[]
for k in range (len(list)-1,0,-1):
    c=1
    for j in range(k,-1,-1):
        if list[k]>list[j]:
           c=c+1
        elif list[k]<list[j]:
            break
    l.append(c)
l.append(1)
print(l[::-1])