n=5
k=5
s_arr=[]
arr=[1,2,2,2,3]
max_len=0
count=0
for i in range(0,n):
    for j in range(i,n):
        m=(arr[i:j+1])
        m=(arr[i:j+1])
        if (sum(m)%k!=0 and len(m)>max_len):
            max_len=len(m)
            count=0
        # modified_arr.append(i)
            # if len(m)>max_len:
                # max_len=len(m) #1 2
                # count=0
            if len(m)==max_len:
                count+=1
# modified_arr=[]
# max_len=0
# count=0
# for i in s_arr:

    # if (sum(i)%k!=0):
    #     # modified_arr.append(i)
    #     if len(i)>max_len:
    #         max_len=len(i) #1 2
    #         count=0
    #     if len(i)==max_len:
    #         count+=1

# print(s_arr)
# print(modified_arr)
print(count)

