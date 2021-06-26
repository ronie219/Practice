# Find Angle MBC
import math
ab = int(input("Enter AB"))
bc = int(input("Enter BC"))
print(round(math.degrees(math.atan(ab/bc))),chr(176),sep="")