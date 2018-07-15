N = 50
N = int(input())

for i in range(2, N):
    flag = True
    m = int((i ** 0.5) + 0.5)
    for j in range(2, m+1):
        if i % j == 0:
            flag = False
            break
    if(flag):
        print(i, end=' ')