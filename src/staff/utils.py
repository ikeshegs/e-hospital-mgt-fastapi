import random
import string


def get_random_number() -> int:
    random_number = random.randint(1, 1000)
    return random_number


def generate_random_password() -> str:
    '''
    Generates a random password having the specified length
    :returns a string>
    '''

    LETTERS = string.ascii_letters
    NUMBERS = string.digits

    password_length: int = 8
    
    alphanumeric = f"{LETTERS}{NUMBERS}"

    # convert alphanumeric from string to list and shuffle
    alphanumeric = list(alphanumeric)
    random.shuffle(alphanumeric)

    # generate random password and convert to string
    random_password = random.choices(alphanumeric, k=password_length)
    random_password = ''.join(random_password)
    return random_password
