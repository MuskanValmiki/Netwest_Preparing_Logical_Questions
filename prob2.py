# sub array
T=int(input("enter any number="))
list=list(map(int,input().split()))
# result=[]
max_length=0
dic={}
for i in range(1,len(list)+1):
    dic[str(i)]=[]
for i in range(0,(len(list))):   
    for j in range(i,len(list)):
        a=list[i:j+1]
        dic[str(len(a))].append(a)
print(dic)
# print(result)