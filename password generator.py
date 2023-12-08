import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(num_passwords, length=12):
    passwords = [generate_password(length) for _ in range(num_passwords)]
    return passwords

def main():
    print("Welcome to the Secure Password Generator!")

    try:
        length = int(input("Enter the desired length of the password: "))
        num_passwords = int(input("Enter the number of passwords to generate: "))

        if length <= 0 or num_passwords <= 0:
            print("Please enter valid values for length and number of passwords.")
            return

        passwords = generate_multiple_passwords(num_passwords, length)

        print("\nGenerated Passwords:")
        for i, password in enumerate(passwords, start=1):
            print(f"{i}. {password}")

    except ValueError:
        print("Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    main()
