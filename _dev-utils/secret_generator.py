import secrets
import string

def generate_secret_key():
    """
    Generates a cryptographically secure 50-character secret key.
    Compatible with Django's SECRET_KEY requirements.
    """
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + '!@#$%^&*(-_=+)'
    secret_key = ''.join(secrets.choice(chars) for _ in range(50))
    return secret_key

if __name__ == "__main__":
    print("\nGenerated Django Secret Key:")
    print("-" * 54)
    print(generate_secret_key())
    print("-" * 54)
    print("Copy the key above and add it to your .env file as SECRET_KEY='<your_key>'\n")



