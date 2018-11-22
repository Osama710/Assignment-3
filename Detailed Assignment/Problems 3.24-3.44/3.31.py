print("Muhammad Osama - 18B-003-CS - Sec'A'")
print("Detailed Assignment")
print("Problem No: 3.31 ")

import math
x = eval(input("Enter x coordinate: "))
y = eval(input("Enter y coordinate: "))
r = 8

cal = math.sqrt(x**2 + y**2)

if cal <= r:
    print("It is in!")
