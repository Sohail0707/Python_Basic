# PRINTING HELLO WORLD
print("hello world")

# MAKING VARTIABLES
age = 21
is_adult = True

# TAKING INPUT ///////////////////////////////////////
# name = input("What is your name?\n")

# print ("Hello " + name )

# CHANGING DATA TYPE /////////////////////////////////
# age = int(input("What is your age ? \n"))

# print("You are "+str(age) +" years old")

#WORKING WITH STRING //////////////////////////////////
name = "Tony Stark"
print(name.upper()) # Convert into uppercase, 
print(name.find("Stark")) # Returns the starting index (starts from 0)
print(name.replace("Tony Stark", "Ironman")) # Replace and return
print('S' in name) # Returns True if 'S' exists in 'name'  else returns 'false'

# tHIS DOES NOT CHANGE THE MAIN STRING
print(name)


# MATHEMATICAL OPERATORS ///////////////////////////////
print(2+3) # Addition
print(3-1) # Subtraction
print(2*3) # Multiplication
print(2/3) # Division
print(2//3) # Returns the integer part after division
print(2%3) # Returns the remender part after division

# LOGICAL OPERATORS ////////////////////////////////////
print(2>3  or 5>3) # Returns true if one condition id true
print(2>3  and 5>3) # Returns true if both condition id true
print(not 5>3) # Reverses the condition return

# IF ELSE STATEMENT
age = 21
if age >= 18: # no need to use {}, use :
    print("You are an adult") # We use indentation to define a block of code
    print("You can vote now")

elif  age < 18 and age >3:
    print("You are teen ager")

else: 
    print("You are a kid")