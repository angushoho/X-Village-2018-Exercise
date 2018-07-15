'''
def f1(a, b=4, c=5):
    print(a, b, c)
f1(1, 2)

def f2(a, b, c=5): 
    print(a, b, c)
f2(1, c=3, b=2)

def f3(a, *args):
    print(a, args)
f3(1, 2, 3)

def f4(a, **kargs): 
    print(a, kargs)
f4(a=1, c=3, b=2)

def f5(a, b, c=3, d=4): 
    print(a, b, c, d)
f5(1, *(5, 6))
'''

def f6(a = 0, **args):
    print(a, args)
args = {'a' : 4, 'b' : 3}

#f6(1, 2, **{a = 4, b = 3})

f6(1, args)