def cal(x, y):
    if x < 0:
        raise ValueError("you should enter positive number")
    else:
        return x % y

a = int(input())
b = int(input())

try:
    num = cal(a, b)
    print(num)
except ValueError as e:
    print(e)
