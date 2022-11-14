L,R=map(int,input().split())
list_odd_number=[]
for number in range(L,R+1):
    if number%2!=0:
        list_odd_number.append(number)
for number2 in list_odd_number:
    print(number2, end=" ")
    

# cook your dish here
L,R=map(int,input().split())
Odd_List=[]
while L<=R:
    if L%2!=0:
        Odd_List.append(L)
    L+=1
print(Odd_List)