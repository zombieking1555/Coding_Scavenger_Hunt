"""
Nice job making it this far! Make sure you remember the last 3 words, because your 4th will be coming soon!
Look carefully through the functions in this file, as you will find the next step in one of them.
"""

leftSpeed = 0.0
rightSpeed = 0.0

def driveForward(speed):
    global leftSpeed, rightSpeed
    leftSpeed = speed
    rightSpeed = speed
    print("Driving forward at speed", speed)

def driveBackward(speed):
    global leftSpeed, rightSpeed
    leftSpeed = -speed
    rightSpeed = -speed
    print("Driving backward at speed", speed)

def turnLeft(speed):
    global leftSpeed, rightSpeed
    leftSpeed = -speed
    rightSpeed = speed
    print("Turning left at speed", speed)

def turnRight(speed):
    global leftSpeed, rightSpeed
    leftSpeed = speed
    rightSpeed = -speed
    print("Turning right at speed", speed)

def nextStep():
    print("The next step is to check the Gyroscope sensor file!")

def stop():
    global leftSpeed, rightSpeed
    leftSpeed = 0
    rightSpeed = 0
    print("Drive stopped.")

# Example run
driveForward(0.5)
turnLeft(0.3)
stop()
