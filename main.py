secret_number = 65

guess = int(input("Guess secret number: "))

if guess == secret_number:
    print("That's correct! Congratulations!")
else:
    print("Better luck next time.")