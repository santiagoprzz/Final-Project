import random

choose_difficulty= input("Choose difficulty (easy / medium / hard): ")
choose_difficulty= choose_difficulty.lower()
max_attempts= None
if choose_difficulty == "hard":
    max_attempts= 7


number= random.randint(1, 100)
attempts= 0
GUESSED= False
valid_input = False

print("THE INCREDIBLE NUMBER GUESSING GAME :D")
print("Are you ready??????")
print("LETS START")
print("Guess a number between 1 and 100")

while GUESSED is not True and (max_attempts is None or attempts < max_attempts):    #While the number has not been guessed and less attempts than 7
    valid_input = False
    guess= input("Please insert your guess: ")

    if guess.isdigit():            
        guess = int(guess)
        valid_input = True
    else:
        print("Please choose a number")

    if valid_input is True:                     
        attempts +=1
        if guess> number:
            print("Too high")
        elif guess < number:
            print("Too low")
        else:
            GUESSED=True
            print("CONGRATS you guessed correctly!!!!!!")
            print(f"It took you {attempts} attempts.")
    
    if attempts> max_attempts:
        print(f"GAME OVER!! Correct answer was: {number}")
