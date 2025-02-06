'''
File Name: workingWithshapes v.2.py;
    
 Purpose: Calculates area of squares and cubes and triangles! User is able to enter in unique values, and 
 choose amongst the available options. Loops to ensure valid inputs. 
 
Requierments: Python 3.1;
 
 File Created: 02/03, 2025;
 Last Updated: 02/04, 2025;  
 Author: Malachi Butler;   

Version 3.1
'''
#area of a square
def square():
    length = int(input("Lengh for Square: "));
    width = int(input("Width for Square: "));
    areaOne = float(length) * float(width)
    return areaOne;

#area of a cube
def cube(): 
    lengthTwo = input("Lengh for Cube: ")
    widthTwo = input("Width for Cube: ")
    heightOne = input("Height of the Cube: ")
    areaTwo = float(lengthTwo) * float(widthTwo) * float(heightOne)
    return areaTwo 

#area of a triangle
def triangle(): 
    lenghtThree = input("Lenght for the Triangle: ")
    widthThree = input("Width for the Triangle: ")
    areaThree = 0.5 * float(widthThree) * float(lenghtThree)
    return areaThree

userInputone = "Square"
userInputtwo = "Cube"
userInputThree = "Triangle"

print("** MAKE SURE TO CAPATALIZE FIRST LETTER!! **")
userInput = str(input("Calculate the area of a Square, Cube, or Triangle? "))

while True:
    try:
        if userInput == userInputone: 
            print("The Area of your Square is: " + str(square()))
            break
        elif userInput == userInputtwo:
            print("The Area of your Cube is: " + str(cube()))        
            break
        elif userInput == userInputThree: 
            print("The Area of your Triangle is: " + str(triangle()))
            break
        else: 
            print("Make sure to capatalize first letter or enter out of three options! ")
            userInput = str(input("Calculate the area of a Square, Cube, or Triangle? "))
    except ValueError: 
        print("Oops! Looks like your finger slipped! Try Again :)")
        continue
