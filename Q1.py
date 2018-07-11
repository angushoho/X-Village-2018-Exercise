import math
a = 1
b = 2
c = -63
'''
x1 = ((-b) + (math.sqrt((b**2) - 4 * a * c))) / (2*a)
x2 = (-b) - (math.sqrt((b**2) - 4 * a * c)) / (2*a)
print(x1,"\n")
print(x2, "\n")
'''

x1 = (-b + ((((b**2) - 4 * a * c))**0.5)) / (2*a)
x2 = (-b - ((((b**2) - 4 * a * c))**0.5)) / (2*a)
print(x1)
print(x2, "\n")