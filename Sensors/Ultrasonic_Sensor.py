rangeInches = 12

def getRange():
    print(f"Ultrasonic range: {rangeInches} inches.")
    return rangeInches

def isObstacleNear():
    if rangeInches <= 5:
        print("Obstacle detected!")
        return True
    else:
        print("Path is clear.")
        return False

# Example run
getRange()
isObstacleNear()
