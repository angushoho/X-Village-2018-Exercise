# 99multi.py
RANGE1 = [1, 3]
RANGE2 = [1, 9]

def calc(a,b):
    return [
        {'sign': '*', 'result':a*b},
    ]

for i in range(RANGE1[0], RANGE1[1] + 1):
    for j in range(RANGE2[0], RANGE2[1] + 1):
        for k in calc(i, j):
            # print(str(i) + k['sign'] + str(j) + '=' + str(k['result']), end="|")
            print("{0:<3}{1:<3}{2:<3}{3:<3}{4:<3}{5:<1}".format(str(i), k['sign'], str(j), '=', str(k['result']), '|'), end=' ')
    print()