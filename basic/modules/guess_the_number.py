def play_guess_the_number():
    import random

    print("Please enter the minimum value:")
    min_val = int(input())
    print("Please enter the maximum value:")
    max_val = int(input())

    random_number = random.randrange(min_val , max_val)

    print(f"I am thinking of a number between {min_val} and {max_val}.")
    print("Can you guess what it is?")

    guessed_correct = False

    while not guessed_correct:
        print("Please enter a number:")
        user_guess = int(input())

        if user_guess < random_number:
            print("Your guess is too low.")
        elif user_guess == random_number:
            print("Congratulations! You guessed my number!")
            guessed_correct = True
        elif user_guess > max_val:
            print("Try again:")
        else:
            print("Your guess is to high.")

def run():
    play_guess_the_number()

if __name__ == "__main__":
  run()