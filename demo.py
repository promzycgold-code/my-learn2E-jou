import random
secret_number = random.randint(1, 100)

print(f"The computer has chosen a secret number")
guess = 0 
while guess != secret_number:
    guess = int(input("guess a specal number: "))
    if guess > secret_number:
        print("Too high try again")
    elif guess < secret_number:
        print("Too low try again")
else:
    print("you guessed right congratulations")

