#17. Write a program that continues to ask for a number until the correct number is guessed.
correct_number = 7

while True:
    # Ask the user to input a number
    guess = int(input("Guess the number: "))
    
    if guess == correct_number:
        print("Congratulations! You guessed the correct number.")
        break  # Exit the loop if the guess is correct
    else:
        print("Incorrect guess. Try again.")
