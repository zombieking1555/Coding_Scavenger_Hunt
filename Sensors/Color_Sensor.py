colorSeen = "red"

def getColor():
    print(f"Color sensor detects: {colorSeen}")
    return colorSeen

def isTargetColor():
    if colorSeen == "blue":
        print("Target color detected!")
    elif colorSeen == "green":
        print("Special color found!")
    else:
        print("Not the target color.")

# Example run
getColor()
isTargetColor()
