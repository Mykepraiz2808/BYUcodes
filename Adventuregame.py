# Adventure Game - Milestone Submission
# This is the first question with choices and follow-up responses.

# Introduction
print("You wake up in a mysterious forest. In front of you, you see a CAVE and a RIVER. Which one do you choose to explore?")

# Get user input and convert it to lowercase for case-insensitive comparison
choice1 = input("Type CAVE or RIVER: ").strip().lower()

# First decision point
if choice1 == "cave":
    print("You enter the dark cave and hear strange noises. Do you want to LIGHT a torch or KEEP walking in the dark?")
    # This will be expanded in the final version
elif choice1 == "river":
    print("You walk toward the river and see a small boat. Do you want to ROW across or FOLLOW the riverbank?")
    # This will be expanded in the final version
else:
    print("That is not a valid choice. Please restart the game and choose either CAVE or RIVER.")
