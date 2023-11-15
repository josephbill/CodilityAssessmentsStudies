def guess_number():
    print("Think of an integer between 0 (inclusive) and 100 (exclusive).")
    
    # Initial range for guessing
    low = 0
    high = 100
    
    while True:
        # Computer's guess using bisection search
        guess = (low + high) // 2
        print(f"Is your secret number {guess}?")
        
        user_feedback = input("Enter 'h' if the guess is too high, 'l' if it's too low, or 'c' if it's correct: ").strip().lower()
        
        if user_feedback == 'c':
            print(f"Great! The computer correctly guessed your secret number, which is {guess}.")
            break
        elif user_feedback == 'h':
            high = guess
        elif user_feedback == 'l':
            low = guess
        else:
            print("Invalid input. Please enter 'h', 'l', or 'c'.")

# Start the guessing game
# guess_number()

# The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive).
#  The computer makes guesses, and you give it input
#  - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!

