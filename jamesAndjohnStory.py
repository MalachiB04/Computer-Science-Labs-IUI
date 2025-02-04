'''
File Name: jamesAndjohnStory

Purpose: 
    File Demonstrates "import random" when generating unique text. 
    It also demonstrates variable storage and recall, 
    simple arithmatic, and combining strings and variables
    to form a mini story. Demonstrates loops with the
    "try" "while" "continue" "except" and "break" commands, preventing 
    user from entering invalid inputs including blank inputs. 

Requirements:
    - Python Anywhere or Python 3.1 installed 
    
First Create Date:  1/29/2025
Last Update Date:   02/03, 2025
Author: Malachi Butler
Version 3.1
'''
print("*** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** ** **")
#generates random elements for some pizzazz
import random
response = random.randint(1, 3); #variable set to generate number then output a response based off of number picked
if response == 1: 
    response = "I think your name is pretty cool!"; 
elif response == 2: 
    response = "I like your name!"; 
elif response == 3:  
    response = " ...Hey! That's my brothers name!"; 

#variables for characters in the story
name_of_james = "James"; #String Variable #Syntax Error if "" are missing from James
name_of_friend = "John"; #Variable used for the name of johns friend
james_age = 25; #Integer Variable for James age in the story 
john_age = 30; # for Johns age in the story
james_height = 70 / 12; #Float Variable for james heighs #70/0 would yeild a runtime error
john_height = 72 / 12; # for Johns height
time_years = (365 * 5) / 365; #variable holds amount of years James and john have been friends

#displaying the story introduction
print("Hello! My name is", name_of_james, "and my friends name is", name_of_friend, "."); 
print("Fun fact about me is that I am 70 inches tall or {:.3}".format(str(james_height)), "feet tall!", "Oh! James is", str(john_height), "feet tall, pretty cool right?"); 
print("I am", james_age, "years old and my friend is", john_age, "years old.")
print("Me and John have been friends for", time_years, "years."); 

#enter your name! Have some fun with it
your_name = input("What is your name?: "); 

#while loop to make sure the user enters a name and not a blank space
while your_name == "": #syntax error if missing :
    print("I'm sorry I didn't catch that. What is your name?"); 
    your_name = input("What is your name?: ");

#Starts next dialog 
print("\n");
print("Oh! Nice to meet you "+ your_name +"!", response); 
print("What are our ages when combined, I wonder?");

#Enter age. Loop incase user input isn't an integer
while True: 
    try:
        user_input = input("How old are you?: "); #allows user to enter input. Has to be integer
        your_age = int(user_input); #create Type Error when input isn't an integer

        if your_age > 0 and your_age < 5:
            print("\n")
            print("Oh! You're a baby haha! Our ages are", james_age + your_age, "when added!") #logic error if I james_age - your_age
            break  # Exit loop after a valid input
        elif your_age >= 5 and your_age < 13:
            print("\n")
            print("Where are your parents? Our ages are", james_age + your_age, "when added! Cool right?") #logic error if I james_age - your_age
            break  # Exit loop after a valid input
        elif your_age >= 13 and your_age < 18:
            print("\n")
            print("Oh man... be prepared for when you grow up haha. Our ages are", james_age + your_age, "when added Cool right?") #logic error if james_age - your_age
            break  # Exit loop after a valid input
        elif your_age >= 18 and your_age < 105:
            print("\n")
            print("You cool! You're an adult like me! Our ages are", james_age + your_age, "when added! Cool right?")
            break  # Exit loop after a valid input
        else:
            print("I think you're lying :( ")
            continue  # Keep asking for input if the age is unrealistic
        
    except ValueError: # This handles invalid input 
            print("I didn't catch that... What is your age?")
            continue  # Keep asking for input if there's an error

#goodbye message 
print("Well anyway, it was nice meeting you", your_name + "!" , "Hope to talk to you again soon!") #calls back your_name one more time to say goodbye :)
print("*** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** ** **") #cute little boarder because why not