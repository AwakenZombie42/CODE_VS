import random
class game:
    def main():
        level = game.input_number("Level: ")
        num = random.randint(1, level)
        guess = 0

        while num != guess:
            guess = game.input_number("Guess: ")
            if guess < num:
                print("Too small!")
            elif guess > num:
                print("Too large!")
            else:
                print("Just right!")

    def input_number(prompt):
        while True:
            try:
                num = int(input(prompt))
                if num > 0:
                    return num
            except ValueError:
                pass

if __name__ == "__main__":
    game.main()