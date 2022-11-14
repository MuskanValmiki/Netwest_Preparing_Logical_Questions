n = int(input())
for i  in range(n):
     x, y = map(int, input().split())
     diff = x-y
     if(x<y):
         diff= 0
     print(diff)