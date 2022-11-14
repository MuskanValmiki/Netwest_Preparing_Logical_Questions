# signal's capacity

# h=[3,5,0,9,8]
# i=0
# while i<len(h):
#     c=0
#     if h[i]<h[i-1]:
#         print(i,i-1,end=" ")
#     i+=1

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