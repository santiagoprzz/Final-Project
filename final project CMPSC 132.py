import random

#Track the high score depending on difficulty
high_scores = {"easy": None, "medium": None, "hard": None}

def proximity_hint(guess,number):   #Function that takes two arguments and selects which hints to give out
    distance= abs(guess -number)
    if distance<= 4:
        print("Super close!")
    elif distance<= 10:
        print("Close")
    else:
        print("Far away")


choose_difficulty= input("Choose difficulty (easy / medium / hard): ")      #Player chooses difficulty
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

    if guess.isdigit():            #Check if input is a number, else ask again
        guess = int(guess)
        valid_input = True
    else:
        print("Please choose a number")

    if valid_input is True:                            #Tracks attempts
        attempts +=1

        #FOR EASY MODE  
        if choose_difficulty=="easy":
            if guess> number:
                print("Too high")
            elif guess< number:
                print("Too low")

        #FOR MEDIUM/HARD MODE
        else:
            proximity_hint(guess, number)
        
        #Win condition
        if guess==number:     
            GUESSED = True
            print("CONGRATS you guessed correctly!!!!!!")
            print(f"It took you {attempts} attempts.")
        
    
if GUESSED is not True:
    print(f"GAME OVER!! Correct answer was: {number}")

#High score conditional statements
if GUESSED is True:
    if high_scores[choose_difficulty] is None or attempts< high_scores[choose_difficulty]:
        high_scores[choose_difficulty]= attempts
        print("Nice! New high score!")
        print(f"Your best score for {choose_difficulty} difficulty is: {high_scores[choose_difficulty]}")
