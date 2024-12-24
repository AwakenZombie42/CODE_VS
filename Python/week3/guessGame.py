def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print('Correct answer!')
            score += 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input('Sorry, wrong answer. Try again: ')
            attempt += 1
    if attempt == 3:
        print('The correct answer is: ', answer)

score = 0
print('Guess the animal')
check_guess(input('Which animal lives at the North Pole? '), 'Polar bear')
check_guess(input('What is the fastest land animal? '), 'cheetah')
check_guess(input('What is the largest animal? '), 'blue whale')
print('Your score is: ', score)