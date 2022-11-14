for _ in range(int(input())):
    a=list(map(int,input().split()))
    if a[0]>a[1] and a[0]>a[2]:
        print("Alice")
    elif a[1]>a[0] and a[1]>a[2]:
        print("Bob")
    else:
        print("Charlie")
        