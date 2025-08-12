pressed = False
clue2 = True

def isPressed():
    if pressed:
        print("Switch is pressed!")
        return True
    
    elif clue2 == True:
        print("You found the second clue, Remember this word and navigate to the ! (Secret word: Falcon)")
        return False
    
    else:
        print("Switch is not pressed.")
        return False

# Example run
isPressed()
