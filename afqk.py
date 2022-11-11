import math
b = 2.5
xn = 1.28
xk = 3.28
x1 = 1.1
x2 = 2.4
x3 = 3.6
x4 = 1.7
x5 = 3.9
while xn <= xk:
    print ((1+(math.sin(b**3 + xn**3))**2)/((b**3 + xn**3)**1/3))
    xn += 0.4
print ((1+(math.sin(b**3 + x1**3))**2)/((b**3 + x1**3)**1/3))
print ((1+(math.sin(b**3 + x2**3))**2)/((b**3 + x2**3)**1/3))
print ((1+(math.sin(b**3 + x3**3))**2)/((b**3 + x3**3)**1/3))
print ((1+(math.sin(b**3 + x4**3))**2)/((b**3 + x4**3)**1/3))
print ((1+(math.sin(b**3 + x5**3))**2)/((b**3 + x5**3)**1/3))
