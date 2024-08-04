import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4")
        return None

    # Characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure the password has at least one character from each category
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Fill the rest of the password length with random characters
    password += random.choices(characters, k=length - 4)

    # Shuffle the password list to avoid predictable patterns
    random.shuffle(password)

    # Convert the list to a string and return
    return ''.join(password)

if __name__ == "__main__":
    password_length = 12  # Set the desired password length
    generated_password = generate_password(password_length)
    if generated_password:
        print(f"Generated Password: {generated_password}")
