"""
Welcome to the 5th checkpoint! Here you will find a camera which sees in black and white. However, 
we are missing the resolution values for the camera! First, add together the number of commas, equal signs, 
colons, and parentheses pairs in this file, not including what is in this introduction. Then, look in the robot 
constants file on the line that matches the number you get to find the resolution values. And, if you look there,
you might even find the third word!
"""

48

cameraAngle = 0
cameraZoom = 1.0
cameraActive = False
cameraResolution = None  # Will be set later

def turnOnCamera():
    global cameraActive
    cameraActive = True
    print("Camera is now on.")

def turnOffCamera():
    global cameraActive
    cameraActive = False
    print("Camera is now off.")

def setAngle(angle):
    global cameraAngle
    cameraAngle = angle
    print("Camera angle set to", angle, "degrees.")

def zoomIn(amount):
    global cameraZoom
    cameraZoom += amount
    print("Zoomed in by", amount, "x.")

def zoomOut(amount):
    global cameraZoom
    cameraZoom -= amount
    print("Zoomed out by", amount, "x.")

def takePicture():
    print("Picture taken.")

def startRecording():
    print("Recording started.")

def stopRecording():
    print("Recording stopped.")

def detectBlackObject():
    print("Detected a black object in view.")

def detectWhiteObject():
    print("Detected a white object in view.")

# TODO: Set cameraResolution to the correct value from constants.py
# Example:
# from constants import CAMERA_RESOLUTION
# cameraResolution = CAMERA_RESOLUTION
