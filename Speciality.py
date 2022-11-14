for _ in range(int(input())):
    l = list(map(int,input().split()))
    maximum = max(l)
    i = l.index(maximum)
    if i==0:
        print("Setter")
    elif i==1:
        print("Tester")
    else:
        print("Editorialist")