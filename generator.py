from typing import Dict, Union
from random import choice


LETTERS = "abcdefghijklmnopqrstuvwxyz"
NUMBERS = "0123456789"
SYMBOLS = "!¡#$%&/=¿?.-,:"
VALID_TYPES = ["uppercase", "lowercase", "number", "symbol"]

config = {
    "length": 8,
    "uppercase": False,
    "lowercase": False,
    "number": False,
    "symbol": False
}

def generate_string(config: Dict[str, Union[int, bool]]):
    letters = [c for c in LETTERS]
    numbers = [n for n in NUMBERS]
    symbols = [s for s in SYMBOLS]

    string = ""
    for char in range(config["length"]):
        char_type = get_random_type(config)
        if char_type == "uppercase":
            string += choice(letters).upper()
        elif char_type == "lowercase":
            string += choice(letters).lower()
        elif char_type == "number":
            string += choice(numbers)
        elif char_type == "symbol":
            string += choice(symbols)
    
    return string

def get_random_type(config):
    valid_types = [type for type in VALID_TYPES if config[type]]
    
    if not valid_types:
        return "lowercase"
    
    return choice(valid_types)

def ask_options():
    while True:
        password_length = input("Enter password length: ")
        try:
            password_length = int(password_length)
            if password_length > 0:
                break
            print("Password length must be a positive integer.")
        except ValueError:
            print("Password length must be a positive integer.")

    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
    include_lowercase = input("Include lowercase letters? (y/n): ").lower() == "y"
    include_numbers = input("Include numbers? (y/n): ").lower() == "y"
    include_symbols = input("Include symbols? (y/n): ").lower() == "y"

    return {
        "length": password_length,
        "uppercase": include_uppercase,
        "lowercase": include_lowercase,
        "number": include_numbers,
        "symbol": include_symbols
    }

def main(config):
    intro_message = "Default config uses length 8 and only lowercase letters."
    use_default_config = input(f"{intro_message}\n Do you wish to enter config? (y/n): ")
    
    if use_default_config.lower() == "y":
        config = ask_options()
    
    password_string = generate_string(config)

    print(f"\n\nGenerated password: {password_string}\n")


if __name__ == "__main__":
    main(config)
