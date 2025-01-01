import os
salt = os.urandom(16).hex()  # Generates a 16-byte salt and converts it to a hex string
print(salt)