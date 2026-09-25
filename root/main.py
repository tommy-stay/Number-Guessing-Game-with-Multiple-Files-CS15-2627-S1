import utils
from score import lose_points, score_rating

score = 100

secret_number = utils.generate_secret_number()

while True:
    if utils.check_user_guess(secret_number):
        break

    else:
        score = lose_points(score)
        print(f"Your points: {score}")

print(f"Your final score is {score}. Good job! Restart code to play again.")
score = score_rating(score)