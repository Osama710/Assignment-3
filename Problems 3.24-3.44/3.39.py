print("Muhammad Osama - 18B-003-CS - Sec'A'")
print("Detailed Assignment")
print("Problem No: 3.39 ")

import math
def collision(x1, y1, r1, x2, y2, r2):
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    rad = (r1 + r2)**2
    if distance <= rad:
        return True
    else:
        return False
    
    
