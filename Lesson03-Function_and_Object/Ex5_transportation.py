def way(trans):
    def distance(dist):
        if trans == 'car':
            rate = 0.24
        elif trans == 'bus':
            rate = 0.03
        elif trans == 'motor':
            rate = 0.06
        return dist * rate
    return distance

trans = input("Transportation : ")
distance  = int(input("Distance : "))

count = way(trans)
print(count(distance))