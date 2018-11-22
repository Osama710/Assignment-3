print("Muhammad Osama - 18B-003-CS - Sec'A'")
print("Detailed Assignment")
print("Problem No: 3.43 ")

import math
def hit(x1,y1,r1,x2,y2):
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    radius = r1**2
    if distance <= radius:
        return True
    else:
        return False
    
