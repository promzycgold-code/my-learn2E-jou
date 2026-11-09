star=[12, 95, 63, 7, 88, 76]
total_turn=len(star)
attempt=0


name= input("welcome Player "f'''Please Enter Players Name? ''')
print ("TADDA!!! welcome", name )

loser = (f"I know you can do better {name}, next try!!!")
guess = None
winner = "Amazing you won!!! congratulatin"

guessed_numbers =[]

while attempt < total_turn:
    guess = int(input("guess a number: "))
    
    attempt += 1
    if not guess in star:
        print(loser)
        break
    else:
        guess = int(input("guess a number: "))
        attempt += 1
        if not guess in star:
            print(loser)
            break



if attempt == total_turn:
    print(winner)