from checker import check_password_strength
from generator import generate_password
from entropy import calculate_entropy
from logger import save_results

from colorama import Fore, Style, init

init()

print("1. Check Password Strength")
print("2. Generate Strong Password")

choice = input("Choose an option: ")

if choice == "1":

    password = input("Enter password: ")

    score, strength, percent, feedback = check_password_strength(password)

    entropy = calculate_entropy(password)

    save_results(password, strength, percent)

    if strength == "Weak":
        print(Fore.RED + strength)

    elif strength == "Medium":
        print(Fore.YELLOW + strength)

    else:
        print(Fore.GREEN + strength)

    print(Style.RESET_ALL)

    print(f"Score: {score}")
    print(f"Strength Level: {percent}%")
    print(f"Entropy: {entropy} bits")

    print("\nFeedback:")
    for item in feedback:
        print("-", item)

elif choice == "2":

    print(generate_password())

else:
    print("Invalid choice")
