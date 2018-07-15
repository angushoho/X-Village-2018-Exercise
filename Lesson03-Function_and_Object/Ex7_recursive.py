def rec(n):
    if n == 1:
        return 1
    else:
        return rec(n - 1) * n
    
N = int(input())
print('ans : ', rec(N))