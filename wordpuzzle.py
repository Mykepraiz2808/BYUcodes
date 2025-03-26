secret_word = "marble"  # Change this to any secret word
attempts = 0

while True:
    guess = input("Guess the secret word: ")
    attempts += 1
    
    if guess.lower() == secret_word.lower():
        print(f"Correct! You guessed the secret word in {attempts} attempts.")
        break