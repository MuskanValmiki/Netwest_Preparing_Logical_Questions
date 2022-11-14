

# here we did cat and mouse question from hackrank.

q=int(input("enter the number="))
i=0
while i<q:
    x=int(input("enter cat a position="))
    y=int(input("enter cat b position="))
    z=int(input("enter mouse c position="))
    if abs(x-z)>abs(y-z):
        print("Cat B")
    elif abs(x-z)<abs(y-z):
        print("Cat A")
    else:
        print("Mouse c")
    i+=1

 
# import sys
# q = int(input().strip())
# for a0 in range(q):
#     x,y,z = input().strip().split(' ')
#     x,y,z = [int(x),int(y),int(z)]
#     if abs(x-z)>abs(y-z):
#         print('Cat B')
#     elif abs(x-z)<abs(y-z):
#         print('Cat A')
#     else:
#         print('Mouse C')