star = [12, 95, 63, 7, 88, 76]
total_turn = len(star)
attempt = 0

name = input("welcome Player "f'''Please Enter Players Name? ''')
print("TADDA!!! welcome", name)

loser = (f"I know you can do better {name}, next try!!!")
guess = None
winner = "Amazing you won!!! congratulatin"

# 1. This list remembers all numbers the player has already guessed
guessed_numbers = []

while attempt < total_turn:
    guess = int(input("guess a number: "))
    attempt += 1

    # 2. Check if the first input is a duplicate
    if guess in guessed_numbers:
        print(f"{guess} You already guessed that number!")
        
        
        
    else:
        guessed_numbers.append(guess) # Remember the valid guess
        
    if not guess in star:
        print(loser)
        break
    else:
        guess = int(input("guess a number: "))
        attempt += 1
        
        # 3. Check if the second input is a duplicate
        if guess in guessed_numbers:
            print("You already guessed that number!")
            print("try again")
            continue
        else:
            guessed_numbers.append(guess) # Remember the valid guess
            
        if not guess in star:
            print(loser)
            break

if attempt == attempt<total_turn:
    print(winner)
