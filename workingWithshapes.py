'''
File Name: workingWithshapes.py
Author: Malachi Butler 
    
 Purpose: Calculates area of squares and triangles. Demonstrates loops by
 restricting user input to proper format (integer or float in this case)
    
Requirements: Python 3.1 
Version 3.1
'''
import math
#area of a square
print("Area of Your Square:")
def square():
    length = input("Lengh: ")
    width = input("Width: ")
    areaOne = float(length) * float(width)
    return areaOne

#loop to ensure integer
while True: 
    try:
        print("The Area of the Square is:",  str(square()))
        break
    except ValueError: 
        print("Try Again :) ")
    continue

#area of a cube
print("\nArea of your Cube:")
def cube(): 
    lengthTwo = input("Lengh for Cube: ")
    widthTwo = input("Width for Cube: ")
    heightOne = input("Height of the Cube: ")
    areaTwo = float(lengthTwo) * float(widthTwo) * float(heightOne)
    return areaTwo 

#loop to ensure integer
while True: 
    try:
        print("The Area of the Cube is:", str(cube()))
        break
    except ValueError: 
        print("Try Again :) ")
    continue

#area of circle
def areaOfaCircle(radius):
    a =math.pi * float(radius** 2)
    return a
 
radius = 23

print(areaOfaCircle)

