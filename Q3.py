# Sorted Substring

# T=int(input())
# for i in range(T):
#     N=int(input())
#     string=input()
#     c=0
#     for j in range(len(string)):
#         if string[j]=="0" and string[j-1]=="1":
#             c+=1 
#     print(c)


T=int(input())
for i in range(T):
    N=int(input())
    string=input()
    c=0
    for j in range(len(string)-1):
        if string[j]>string[j+1]:
            c+=1 
    print(c)
    