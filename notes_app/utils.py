from cryptography.fernet import Fernet

from django.conf import settings


# Function to encrypt the note
def encrypt_note(note, key=settings.CRYPTO_KEY):
    """
    Generates and returns the encrypted note as bytes
    :param note: the note to encrypt
    :param key: the key to use
    :return: encrypted note string
    """
    fernet_object = Fernet(key)
    return fernet_object.encrypt(note.encode('utf-8'))


def decrypt_note(note, key=settings.CRYPTO_KEY):
    """
    Returns the decrypted note according to our encryption key
    :param note: The encrypted message to be decrypted
    :param key: The key used for encryption
    :return: Decrypted message
    """
    fernet_object = Fernet(key)
    return fernet_object.decrypt(note).decode()
