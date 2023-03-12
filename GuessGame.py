import random

MAX_ATTEMPTS = 10
Excellent_LEVEL = 2
Good_LEVEL = 4
Bad_LEVEL = 7

def level(attempts):
    if attempts <= Excellent_LEVEL:
        return 'Excellent'
    elif attempts <= Good_LEVEL:
        return 'Good'
    elif attempts <= Bad_LEVEL:
        return 'Not bad'
    else:
        return 'Try more'

print('Number Guessing Game')

number = random.randint(1, 100)
guess = None
attempts = 0

while guess != number:
    if attempts > 10:
        print('')
    guess = int(input('Enter your guess(between 1 and 100): '))
    attempts += 1

    if guess > number:
        print(f"Guess a smaller number ({attempts}/10).")
    elif guess < number:
        print(f"Guess a bigger number ({attempts}/10).")
    else:
        message = level(attempts)
        print(f"{message}, You won after {attempts} tries.")
    print("-------------------------------------------\n")
