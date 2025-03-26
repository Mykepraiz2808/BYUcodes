"""
Welcome to the Adventure Game!
This game has been tested by two players who found it both exciting and unpredictable.
Every choice leads to a different path, so choose wisely!
"""

def adventure_game():
    print("Welcome to the Mysterious Cave! You find yourself at a crossroads.")
    print("Do you go LEFT, RIGHT, or STRAIGHT?")
    choice1 = input("Enter your choice: ").strip().lower()
    
    if choice1 == "left":
        print("\nYou have entered a dark tunnel with glowing crystals on the walls.")
        print("A river blocks your path. Do you SWIM across or BUILD a raft?")
        choice2 = input("Enter your choice: ").strip().lower()
        
        if choice2 == "swim":
            print("\nThe water is freezing! You barely make it across and find a hidden treasure chest.")
        elif choice2 == "build":
            print("\nYour raft floats well! You paddle across safely and discover an ancient map.")
        else:
            print("\nConfused, you turn back and leave the cave. The adventure ends.")
    
    elif choice1 == "right":
        print("\nYou enter a chamber filled with ancient ruins and strange markings.")
        print("You see a lever and a button. Do you PULL the lever or PRESS the button?")
        choice2 = input("Enter your choice: ").strip().lower()
        
        if choice2 == "pull":
            print("\nA hidden door opens, leading to a golden staircase descending into the unknown!")
        elif choice2 == "press":
            print("\nA trapdoor opens beneath you, and you fall into a soft pile of feathers. Lucky escape!")
        else:
            print("\nUnable to decide, you hear footsteps approaching. You run away, ending your journey.")
    
    elif choice1 == "straight":
        print("\nYou walk deeper into the cave and find a sleeping dragon!")
        print("Do you FIGHT the dragon or SNEAK past it?")
        choice2 = input("Enter your choice: ").strip().lower()
        
        if choice2 == "fight":
            print("\nBravely, you charge at the dragon but it wakes up and roars! It respects your courage and lets you pass.")
        elif choice2 == "sneak":
            print("\nSilently, you tiptoe past the dragon and discover a hidden exit leading to safety!")
        else:
            print("\nYour hesitation alerts the dragon! You run back the way you came, ending your adventure.")
    
    else:
        print("\nInvalid choice. You hesitate too long, and the cave entrance collapses. Game over!")

# Run the game
adventure_game()
