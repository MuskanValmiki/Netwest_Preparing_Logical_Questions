# sub array 

# T=int(input("enter any number="))
# list=list(map(int,input().split()))
# N=(len(list)/2) 
# k=0
# dic={}
# while k<len(list):
#     j=0
#     c=0
#     while j<len(list):
#         if list[k]==list[j]:
#             c+=1
#         j+=1
#     dic[list[k]]=c
#     k+=1
# for key in dic:
#     if N>dic[key]:
#         print(-1)
#         break
#     else:
#         print(key)
#         break

T=int(input("enter any number="))
list=list(map(int,input().split()))
result=[]
for i in range(1,2**(len(list))):
    a=str(bin(i)[2:])[::-1]
    # print(a)
    temp_arr=[]
    for i in range(0,len(a)):
        if a[i]=="1":
            temp_arr.append(int(list[i]))
    result.append(temp_arr)
print(result)
            