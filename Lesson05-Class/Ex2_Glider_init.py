class Map:
    def __init__(self, size, action):
        self.size = size
        self.list = [[1] * size for i in range(size)]
        if action is 1:
            center = ((self.size) // 2)
            self.set_z(center, -1, -1)
            self.set_z(center, -1, 0)
            self.set_z(center, -1, 1)
            self.set_z(center, 0, -1)
            self.set_z(center, 1, 0)
    def display(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.list[i][j] is 1:
                    print("* ", end="")
                else:
                    print("0 ", end="")

            print("")

    def set_z(self, pos, _x, _y):
        self.list[pos + _x][pos + _y] = 0


n = int(input())
    
new_map = Map(n, 1)

new_map.display()