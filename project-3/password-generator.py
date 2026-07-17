# 🔐 Advanced Menu-Based Password Generator
# This version is written in a more "human-like" style with clear comments
# It includes:
# - Menu system
# - Input validation (no 0 or negative length)
# - Secure password generation (using secrets)
# - Copy to clipboard feature
# - Clean structure and readability

import os
import string
import secrets

# Try importing clipboard library (optional feature)
try:
    import pyperclip
    CLIPBOARD_AVAILABLE = True
except ImportError:
    CLIPBOARD_AVAILABLE = False


# Function to clear the screen (works on Windows & Linux/macOS)
def clear():
    os.system("cls" if os.name == "nt" else "clear")


# Function to generate a strong password
def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ""     # This will store all allowed characters
    password = []       # This will store the final password characters

    # Add character sets based on user choice
    if use_upper:
        characters += string.ascii_uppercase
        password.append(secrets.choice(string.ascii_uppercase))  # ensure at least one

    if use_lower:
        characters += string.ascii_lowercase
        password.append(secrets.choice(string.ascii_lowercase))

    if use_digits:
        characters += string.digits
        password.append(secrets.choice(string.digits))

    if use_symbols:
        characters += string.punctuation
        password.append(secrets.choice(string.punctuation))

    # If user didn't select anything, return error
    if not characters:
        return None

    # Fill the rest of the password length
    remaining_length = length - len(password)

    for _ in range(remaining_length):
        password.append(secrets.choice(characters))

    # Shuffle to avoid predictable pattern
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)


# Function to display menu
def show_menu():
    print("\n===== Password Generator Menu =====")
    options = [
        "Generate Password",
        "View Tips for Strong Password",
        "Exit"
    ]

    # Using enumerate to make numbering clean
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")


# Function to show password tips
def show_tips():
    clear()
    print("🔐 Strong Password Tips:\n")
    print("- Use at least 8–12 characters")
    print("- Mix uppercase and lowercase letters")
    print("- Include numbers and symbols")
    print("- Avoid using personal information")
    input("\nPress Enter to go back...")


# Function to copy password to clipboard
def copy_to_clipboard(password):
    if CLIPBOARD_AVAILABLE:
        pyperclip.copy(password)
        print("Password copied to clipboard!")
    else:
        print("Clipboard feature not available (install 'pyperclip' to enable it)")


# Main program loop
def main():
    clear()

    while True:
        show_menu()

        # Handle invalid menu input safely
        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        # Option 1: Generate Password
        if choice == 1:
            try:
                length = int(input("Enter password length: "))

                # Prevent invalid lengths
                if length <= 0:
                    print("Password length must be greater than 0!")
                    continue

            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

            # Ask user for customization
            use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
            use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
            use_digits = input("Include numbers? (y/n): ").lower() == 'y'
            use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

            password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)

            clear()

            if password:
                print("Generated Password:\n")
                print(password)

                # Ask if user wants to copy it
                copy_choice = input("\nCopy to clipboard? (y/n): ").lower()
                if copy_choice == 'y':
                    copy_to_clipboard(password)
            else:
                print("You must select at least one character type!")

            input("\nPress Enter to continue...")

        # Option 2: Show Tips
        elif choice == 2:
            show_tips()

        # Option 3: Exit
        elif choice == 3:
            clear()
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")


# This ensures the program only runs when executed directly
if __name__ == "__main__":
    main()