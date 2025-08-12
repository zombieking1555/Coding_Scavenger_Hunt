distance = 42  # fake distance in centimeters

def getDistance():
    print(f"Distance sensor reads {distance} cm.")
    return distance

def isTooClose():
    if distance < 20:
        print("Warning: Too close!")
        return True
    return False

# Example run
getDistance()
isTooClose()
