'''
x = int(input())
y = int(input())
#print(type(x))
#print(type(y))
'''

A = [-1, -10]
B = [5, -5]
C = [1, 1]
D = [-2, 3]

dot_set = [A, B, C, D]

for dot in dot_set:
    print(dot, "is in ", end="")
    if dot[0] == 0:
        print("on y ")
        continue
    if dot[1] == 0:
        print("on x ")
        continue
    if(dot[0] > 0):
        if(dot[1] > 0):
            print("1\n")
        else:
            print("4\n")
    elif dot[0] < 0:
        if(dot[1] > 0):
            print("2\n")
        else:
            print("3\n")

    
