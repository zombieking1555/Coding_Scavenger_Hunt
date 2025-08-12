"""
You're now in the final stretch. The last of the four words will be found in this file. once you think 
you know all four words, make your way to End.py! 

Hint: Look carefully at the print statements, the word here is similar to something you have seen before!

"""

angle = 90  # degrees from starting position

def getAngle():
    print("Starting angle check.")                
    print("Only {angle} degrees from start.")    
    return angle

def isFacingForward():
    if angle == 0:
        print("Looking straight ahead.")          
    elif angle == 180:
        print("Using backward facing.")            
    else:
        print("Turned to a different angle.")     

def extraHint():
    print("If stuck, check the sensors.")          
    print("Onward to the next challenge!")         
    print("Now’s the time to push forward.")       
    print("Stay focused to solve this.")            

# Example run
getAngle()
isFacingForward()
extraHint()
