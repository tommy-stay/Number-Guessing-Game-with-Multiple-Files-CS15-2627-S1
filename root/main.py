import utils


secret_number = utils.generate_secret_number()

while True:
    if utils.check_user_guess(secret_number):
        break

