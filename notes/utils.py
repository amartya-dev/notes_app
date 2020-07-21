from cryptography.fernet import Fernet

from django.conf import settings


# Get the generated key
def get_generated_key():
    """
    Generte a key for encrypting and decrypting messages
    :return: Encryption key
    """
    with open('secret.key', 'rb') as key_file:
        KEY = key_file.read()
        return KEY


# Function to encrypt the note
def encrypt_note(note, key=settings.CRYPTO_KEY):
    """
    Generates and returns the encrypted note
    :param note: the note to encrypt
    :param key: the key to use
    :return: encrypted note string
    """
    fernet_object = Fernet(key)
    return fernet_object.encrypt(note)
