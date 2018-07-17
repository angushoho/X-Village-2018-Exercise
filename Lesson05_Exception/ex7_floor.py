class FallDownException(Exception):
    def __init__(self, floor):
        self.msg = "在 {} 樓被接住了".format(floor)

    def __str__(self):
        return self.msg

class FallDownStrongerException(Exception):
    def __init__(self, floor):
        self.msg = "在 {} 樓被接住了".format(floor)
    def __str__(self):
        return self.msg

def slip(floor):
    try:
        while floor:
            floor -= 1
            print("現在在 {} 樓".format(floor))

            if floor == 80:
                raise FallDownException(floor)
                
    except FallDownException as e:
        print(e)
        print("突破機關！")
        while floor:
            floor -= 1
            print("現在在 {} 樓".format(floor))
            
            if floor == 5:
                raise FallDownStrongerException(floor)
     
# TODO: 用 try...except 把 slip(106) 包起來
try:
    slip(106)
except FallDownStrongerException as e:
    print(e)
    print("安全")