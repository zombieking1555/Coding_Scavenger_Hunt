# Fake climbing subsystem
"""
You are now at checkpoint 4! Hopefully you remember the first word you got, because you will be finding the second
one in this file! You will see that each of the functions (Denoted by the word "def", remember!) are being described
very specifically in this subsystem with print() statements. To find your second of four words, look at the first letter
of each print statement! Then, look again to the print statements to get the next file to navigate to.

"""

climbHeight = 0
climbSpeed = 0.0
hooksEngaged = False

def engageHooks():
    global hooksEngaged
    hooksEngaged = True
    print("Engaging hooks for climbing.")   

def notchPosition():
    print("Notching position for stability.")  

def gripBar():
    print("Gripping the climbing bar.")    

def initiateLift():
    global climbHeight, climbSpeed
    climbSpeed = 0.8
    climbHeight = 10
    print("Initiating lift upwards.")       

def nudgeHigher():
    global climbHeight
    climbHeight = 15
    print("Nudging height higher.")         

def elevateFurther():
    global climbHeight
    climbHeight = 20
    print("Elevating to final height.")    

def engageLatch():
    print("Engaging final latch. Go navigate to the Camera subsystem!")          

def releaseHooks():
    global hooksEngaged
    hooksEngaged = False
    print("Releasing hooks.")               

def insertArm():
    print("Inserting arm into storage.")    

def nudgeIntoPlace():
    print("Nudging into final position.")   

def grabSupport():
    print("Grabbing support bar.")          

# Example run in order
engageHooks()
notchPosition()
gripBar()
initiateLift()
nudgeHigher()
elevateFurther()
engageLatch()
releaseHooks()
insertArm()
nudgeIntoPlace()
grabSupport()