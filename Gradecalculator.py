# Ask the user for their grade percentage
percentage = float(input("Enter your grade percentage: "))

# Determine the letter grade
if percentage >= 90:
    letter = "A"
elif percentage >= 80:
    letter = "B"
elif percentage >= 70:
    letter = "C"
elif percentage >= 60:
    letter = "D"
else:
    letter = "F"

# Determine the sign (+ or -), but exclude A+ and F+/- cases
sign = ""
last_digit = percentage % 10

if letter != "A" and letter != "F":  # A+ doesn't exist, and F has no +/-
    if last_digit >= 7:
        sign = "+"
    elif last_digit < 3:
        sign = "-"

# Print the final letter grade
print(f"Your grade is: {letter}{sign}")

# Check if the student passed
if percentage >= 70:
    print("Congratulations! You passed the class.")
else:
    print("Keep working hard! You'll get it next time.")
