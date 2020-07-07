# comments start with #, not //
#import otherLocalFile.py
#import externalLibrary

# Variable Declarations: just type the variable name and assign it a value!
x = 4

# Lists: https://www.w3schools.com/python/python_lists.asp
# Pythons lists can store different types in the same list
volatiles = ["Oxygen", "Hydrogen", 7]
print(volatiles[1])
# Python lists loop! -1 accesses the last element in the array
print(volatiles[-1])

# Tuples: https://www.w3schools.com/python/python_tuples.asp
roverTypes = ("Scout", "Hauler")
print(roverTypes[0:2]) # this prints a range, inclusiveIndex to exclusiveIndex

# Dictionaries: https://www.w3schools.com/python/python_dictionaries.asp
# Sort of like structs
roverDetails = {
"isRoverOn" : False,
"roverName" : "Adelaide",
}
print(roverDetails["roverName"])

# Functions start with def
# Python does not require line ending characters or curly braces
# for functions, loops, or if statements
# indents and : characters are used in their place
def printValue(duration):
    # rather than && and ||, words are used, e.g. "and" and "or"
    k = 0
    while((k < duration) and (True)):
        k += 1
        if((k % 2) == 0):
            print("k is even")
        else:
            print("k is odd")
        print(k)

def ForLoop():
    for i in range(x):
        print("hello")

w = 5
printValue(w)
ForLoop()
