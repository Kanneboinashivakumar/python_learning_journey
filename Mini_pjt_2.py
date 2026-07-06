#Random Password Generator

import random
import string

characters = string.ascii_letters + string.digits + string.punctuation
password_length = int(input("Enter the desired password length: "))

password = ''.join(random.choice(characters) for _ in range(password_length))
print("Generated Password:", password)