import random

number= random.randint(1, 100)
attempts= 0
guessed_correctly= False
valid_input = False

print("THE INCREDIBLE NUMBER GUESSING GAME :D")
print("Are you ready??????")
print("LETS START")
print("Guess a number between 1 and 100")

while guessed_correctly is not True:    #While the number has not been guessed
    valid_input = False

    guess= input("Please insert your guess: ")

    if guess.isdigit():
        guess = int(guess)
        valid_input = True
    else:
        print("Invalid input. Enter a number.")

    if valid_input:
        attempts += 1

        if guess> number:
            print("Too high")
        elif guess < number:
            print("Too low")
        else:
            guessed_correctly = True
            print("CONGRATS you guessed correctly!!!!!!")