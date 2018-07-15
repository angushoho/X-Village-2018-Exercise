def foo(m):
    for i in range(1, m+1):
        for j in range(1, m+1):
            print(i, " * ", j , " = ", i * j, end='   ')
        print()
m = 1
while m > 0:
    m = int(input("input number : "))
    foo(m)