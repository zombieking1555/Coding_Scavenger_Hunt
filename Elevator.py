# Elevator - Checkpoint 1

"""

In robot programming, there are things called Functions. They are used to make robots do things, 
and each function is indicated with the word "Def". Count the number of functions in this elevator subsystem and
then navigate to that number sensor in the sensors folder!

"""

elevatorHeight = 0  # 0 is bottom, bigger numbers are higher

def goToTop():
    global elevatorHeight
    print("Going up...")
    elevatorHeight = 10
    print("Reached the top!")

def goToBottom():
    global elevatorHeight
    print("Going down...")
    elevatorHeight = 0
    print("Reached the bottom!")

def moveToHeight(height):
    global elevatorHeight
    print(f"Moving to height {height}...")
    elevatorHeight = height
    print(f"Now at height {elevatorHeight}.")

def manualControl(direction):
    global elevatorHeight
    if direction == "up":
        elevatorHeight += 1
        print(f"Going up! Height is now {elevatorHeight}")
    elif direction == "down":
        elevatorHeight -= 1
        print(f"Going down! Height is now {elevatorHeight}")
    else:
        print("Stopped.")

# Example use:
goToTop()
manualControl("down")
moveToHeight(5)
goToBottom()

