t = int(input())
for i in range(t):
    x,y = map(int, input().split())
    if x<y:
        print("NO")
    else:
        print("YES")