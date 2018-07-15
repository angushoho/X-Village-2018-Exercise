def f(a, b):
    if a > b:
        return "a > b"
    elif a < b:
        return "a < b"
    else:
        return "a = b"

x = int(input())
y = int(input())
msg = f(x, y)
print(msg)