import random

ans = random.randint(1, 100)
x = -1
print(ans)
while x != ans:
    x = int(input("enter a number : "))
    if(x > 100 or x < 0):
        print("number is in 1 ~ 100")
        continue
    if(x > ans):
        print("too big")
        continue
    if(x < ans):
        print("too small")
        continue
    print("correct")