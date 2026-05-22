def check_password_strength(password):

    score = 0
    feedback = []

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"

    common_passwords = [
        "123456",
        "password",
        "qwerty",
        "admin"
    ]

    if password.lower() in common_passwords:
        feedback.append("This password is too common")
        score = 0

    for char in password:

        if char.isupper():
            has_upper = True

        elif char.islower():
            has_lower = True

        elif char.isdigit():
            has_digit = True

        elif char in special_characters:
            has_special = True

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")

    if len(password) >= 12:
        score += 1

    if has_upper:
        score += 1
    else:
        feedback.append("Add uppercase letters")

    if has_lower:
        score += 1
    else:
        feedback.append("Add lowercase letters")

    if has_digit:
        score += 1
    else:
        feedback.append("Add numbers")

    if has_special:
        score += 1
    else:
        feedback.append("Add special characters")

    max_score = 6
    percent = int((score / max_score) * 100)

    if percent <= 40:
        strength = "Weak"

    elif percent <= 70:
        strength = "Medium"

    else:
        strength = "Strong"

    return score, strength, percent, feedback
