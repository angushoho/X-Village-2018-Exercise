N = 8

def check(position):
    is_attack = True

    """ check row and colunm """
    x_list = []
    y_list = []
    for i in range(N):
        x = position[i][0]
        y = position[i][1]
        if x in x_list:
            return False
        x_list.append(x)

        if y in y_list:
            return False
        y_list.append(y)
    
    for i in range(N):
        for j in range(i+1, N):
            c = abs((x - position[j][0]) / (y - position[j][1]))
            if c == 1.0:
                return False
        

    return True

position = [[None] * 2 for i in range(N)]

for i in range(N):
    for j in range(2):
        # print(i , j)
        position[i][j] = int(input())
        
#status = check(position)
#print(status)

print(check(position))