import random

MAX = 100
MIN = 1


def generate_secret_number():
   secret_number = random.randint(MIN, MAX)
   return secret_number

def check_user_guess(secret_number):
   guess = prompt_valid_guess()
   if guess == secret_number:
       print("Correct!")
       print(f"You guessed the number {secret_number}")
       return True
   elif guess < secret_number:
       print("Too low!")
   else:
       print("Too high!")
   return False



def prompt_valid_guess():
   while True:
       print(f"Guess a number between {MIN} and {MAX}")
       guess = input()
       try:
           guess = int(guess)
       except ValueError:
           print("Invalid guess.")
           print("Guess must be a number!")
           continue
       if guess > MAX:
           print("Invalid guess.")
           print(f"Out of range, cannot be greater than {MAX}")
           continue
       if guess < MIN:
           print("Invalid guess.")
           print(f"Out of range, cannot be lower than {MIN}")
           continue
       return guess

if __name__ == "__main__":
    number_to_print = generate_secret_number()


    for i in range(3):
        check_user_guess(number_to_print)

