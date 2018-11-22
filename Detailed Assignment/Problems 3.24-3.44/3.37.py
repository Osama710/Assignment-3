print("Muhammad Osama - 18B-003-CS - Sec'A'")
print("Detailed Assignment")
print("Problem No: 3.37 ")

import math
def points(x1, y1, x2, y2):
    distance = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
    if x2 == 0:
        print("The slope is Infinity and the  distance is ", distance)
    else:
        slope = ((y2-y1)/(x2-x1))
        print("The slope is ", slope, "and the distance is ", distance)

