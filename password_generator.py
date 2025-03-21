import random
import string
from colorama import Fore, Style, init

init(autoreset=True)

def get_yes_no_input(prompt):
    while True:
        response = input(prompt).lower()
        if response in ('y', 'n'):
            return response == 'y'
        print(Fore.RED + "Please enter 'y' or 'n'!")

def generate_password(length, use_upper, use_lower, use_digits, use_special):
    char_sets = []
    if use_upper: char_sets.append(string.ascii_uppercase)
    if use_lower: char_sets.append(string.ascii_lowercase)
    if use_digits: char_sets.append(string.digits)
    if use_special: char_sets.append(string.punctuation)

    if not char_sets:
        raise ValueError(Fore.RED + "At least one character type must be selected!")
    
    password = []
    for charset in char_sets:
        password.append(random.choice(charset))
    
    all_chars = ''.join(char_sets)
    password += random.choices(all_chars, k=length - len(password))

    random.shuffle(password)
    return ''.join(password)

def main():
    print(Fore.CYAN + Style.BRIGHT + "\n=== SECURE PASSWORD GENERATOR ===")
    try:
        length = int(input(Fore.WHITE + "\nEnter password length (8 - 64): "))
        if not 8 <= length <= 64:
            raise ValueError
    except ValueError:
        print(Fore.RED + "Invalid length! Using default 12 characters.")
        length = 12

    print(Fore.YELLOW + "\nSelect character types to include: ")
    use_upper = get_yes_no_input("Include uppercase letters? (y/n): ")
    use_lower = get_yes_no_input("Include lowercase letters? (y/n): ")
    use_digits = get_yes_no_input("Include digits? (y/n): ")
    use_special = get_yes_no_input("Include special characters? (y/n): ")

    try:
        password = generate_password(length, use_upper, use_lower, use_digits, use_special)
        print(Fore.GREEN + Style.BRIGHT + "\nGenerated password: " + Fore.MAGENTA + password)
        print(Fore.YELLOW + f"Length: {len(password)} characters | Entropy: {length * 4} bits")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()