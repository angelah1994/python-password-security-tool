def save_results(password, strength, percent):

    with open("password_log.txt", "a") as file:

        file.write(
            f"Password: {password} | "
            f"Strength: {strength} | "
            f"Score: {percent}%\n"
        )
