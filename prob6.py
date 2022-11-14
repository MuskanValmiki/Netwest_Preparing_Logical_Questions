T=int(input("enter any number="))
list=list(map(int,input().split()))
l=[0,0,0,0,0,0,0,0,0,0]
for i in list:
    l[i%10]+=1
    i+=1
print(l)
