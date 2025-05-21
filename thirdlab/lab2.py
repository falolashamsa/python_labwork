import random

secret_num = random.randint(1, 20)
amount_of_guess = 5

print(f"""Hello!
Welcome to Shamsa's Guessing Game
Here, I'll think of a number between 1 and 20 (1 and 20 inclusive)
You have {amount_of_guess} attempts to guess it.\n""")

for amount in range(1, 6):
    guess = int(input(f"Input no.{amount} guess: "))

    if guess == secret_num:
        print(f" Correct! you guessed the number right on {amount} try")
    else:
        print("Guess again!")

else:
    print(f"You've used up all of your guesses, the number was {secret_num}. Come back next time.")