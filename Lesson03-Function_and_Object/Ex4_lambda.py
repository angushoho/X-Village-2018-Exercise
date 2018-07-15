'''
def foo(n):
    def bar(x):
        return n ** x
    return bar
'''
def foo(n):
    return lambda x: n ** x

N = int(input())
f = foo(N)
M = int(input())
print(f(M))