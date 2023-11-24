import random
import string

def generated_access_code(length=6):
    letters_and_digits = string.ascii_letters + string.digits
    access_code = "23mn45"
    access_code_one = ''.join(random.choice(letters_and_digits) for _ in range(length))
    return access_code
