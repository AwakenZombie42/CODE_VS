from random import randint

import time

# Generate a random number between 1 and 100
number = randint(1, 100)

# Ask the user to guess the number
guess = int(input("Guess a number between 1 and 100: "))

# Keep track of the number of guesses
guesses = 1

# Start the timer
start_time = time.time()

# Loop until the user guesses the correct number
while guess != number:
    if guess < number:
        print("Too low!")
    else:
        print("Too high!")
    guess = int(input("Guess again: "))
    guesses += 1

# Stop the timer
end_time = time.time()

# Calculate the time it took to guess the number
time_taken = end_time - start_time

# Print the results
print("You guessed the number in", guesses, "guesses!")
print("It took you", time_taken, "seconds to guess the number.")