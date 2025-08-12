# Intaking subsystem
"""
Congrats on making your way to checkpoint 3! in this Subsystem, which is what we call different parts of a robot,
you will find a lot of addition to variables. find the number of = signs, and then subtract the number of + signs from it
to get the number of characters in the name of the next file you must navigate to! (.py is also characters)

Hint: The signs in this introduction are also counted!
"""

gamePiecesHeld = 0  # how many pieces the intake currently has
intakeSpeed = 0.0   # speed of intake motor (1.0 to 1.0)

def intakeIn():
    global gamePiecesHeld, intakeSpeed
    intakeSpeed = 0.5
    print("Intake running forward.")
    gamePiecesHeld = gamePiecesHeld + 1
    print(f"Now holding {gamePiecesHeld} game piece(s).")

def intakeOut():
    global gamePiecesHeld, intakeSpeed
    intakeSpeed = 0.5
    print("Intake running backward.")
    gamePiecesHeld = gamePiecesHeld - 1
    if gamePiecesHeld < 0:
        gamePiecesHeld = 0
    print(f"Now holding {gamePiecesHeld} game piece(s).")

def stopIntake():
    global intakeSpeed
    intakeSpeed = 0.0
    print("Intake stopped.")

def adjustCount(amount):
    """Manually adjust the count, can be positive or negative."""
    global gamePiecesHeld
    gamePiecesHeld = gamePiecesHeld + amount
    if gamePiecesHeld < 0:
        gamePiecesHeld = 0
    print(f"Adjusted count to {gamePiecesHeld}.")

def overIntake():
    """Pretend to pick up multiple pieces in a row."""
    global gamePiecesHeld
    gamePiecesHeld = gamePiecesHeld + 3
    print(f"Over intake! Now holding {gamePiecesHeld} game pieces.")

# Example run
intakeIn()
intakeIn()
intakeOut()
overIntake()
adjustCount(-2)
stopIntake()
