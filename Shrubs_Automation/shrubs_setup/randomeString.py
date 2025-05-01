import random
import string

def random_string_generator(size=5, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

email = random_string_generator() + '@yopmail.com'


def random_username_generator(length=8):
    # Define the characters that will be used in the username (letters and digits only)
    characters = string.ascii_letters + string.digits
    username = ''.join(random.choice(characters) for i in range(length))

    # Optionally, ensure the username starts with a letter (if that's a requirement)
    if username[0].isdigit():
        username = random.choice(string.ascii_letters) + username[1:]

    return username


# Example usage: Generate a random username of length 10
random_username = random_username_generator(10)


def random_password_generator(length=12):
    # Ensure the length is at least 8
    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")

    # Define the character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure the password contains at least one character from each set
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the remaining password length with random characters from all sets
    all_characters = uppercase + lowercase + digits + special_characters
    password += [random.choice(all_characters) for i in range(length - 4)]

    # Shuffle the password to ensure randomness
    random.shuffle(password)

    # Join the list into a string and return the password
    return ''.join(password)

# Example usage: Generate a random password of length 12
random_password = random_password_generator(12)


# Example usage: Generate a random password of length 12
