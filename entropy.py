import math

def calculate_entropy(password):

    charset_size = 0

    if any(char.islower() for char in password):
        charset_size += 26

    if any(char.isupper() for char in password):
        charset_size += 26

    if any(char.isdigit() for char in password):
        charset_size += 10

    if any(char in "!@#$%^&*()" for char in password):
        charset_size += 10

    entropy = len(password) * math.log2(charset_size)

    return round(entropy, 2)
