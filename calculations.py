# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass

import math

height = slider.value()
inches = height * 39.37
feetinches = inches // 12
leftoverinches = inches %12
print ("This is how tall you are in inches: ",inches)
print ("This is how tall you are in ft", math.trunc(feetinches), "ft", math.trunc(leftoverinches), "Inches")
