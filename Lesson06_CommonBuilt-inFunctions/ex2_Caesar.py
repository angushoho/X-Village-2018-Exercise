# ord(char)
# chr(char)

def caesar_cipher(str, num):
    new = ""
    for i in range(len(str)):
        order = ord(str[i])
        after = order + num
        print("after : ", after, end=' ')
        '''
        if after > 122:
            after = (after - 122) % 26 + 96
        '''
        after = ((after + 26) - 122) % 26 + 96
        if after == 96:
            after = 122
        new += chr(after)
        print(after)

    return new


str = input()
n = int(input())
after = caesar_cipher(str, n)
print(after)