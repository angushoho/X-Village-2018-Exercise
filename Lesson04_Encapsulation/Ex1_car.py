class Car:
    color = None
    __speed = None
    def __init__(self, color):
        self.Color = color
        self.speed = 0
    
    def boost(self, speed):
        if speed < 0:
            print("you can't boost negative speed")
            return None
        self.speed += speed

    def step_break(self, speed):
        if speed < 0:
            print("you should input positive number")
            return None
        self.speed -= speed

    def get_speed(self):
        return self.speed

    def set_speed(self, newspeed):
        if newspeed < 0 or newspeed > 100:
            print("please input correct speed")
            return None
        self.speed = newspeed

yello_car = Car("yello")
red_car = Car("red")

# print("car 1 : ", yello_car.Color.ljust, yello_car.speed, sep=' ')
# print("car 2 : ", red_car.Color, red_car.speed, sep=' ')

# yello_car.boost(-1)
# print(yello_car.speed)
# red_car.step_break(-1)
# print(red_car.speed)

yello_car.set_speed(50)
print(yello_car.get_speed())
# yello_car.__speed