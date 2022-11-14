# T=int(input())
# for i in range(T):
#     A,B=map(int,input().split())
#     if A==B:
#         print(7-A)
#     elif A>B:
#         print(7-A)
#     else:
#         print(print(7-B))


t = int(input())
for test in range(t):
    x,y = map(int,input().split())
    print(min(7-x,7-y))