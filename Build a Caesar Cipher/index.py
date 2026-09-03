# Caesar Cipher
# ----------------
# A Caesar cipher is a simple encryption technique.
# It shifts each letter in the alphabet by a fixed number
# of positions.
#
# Example with a shift of 5:
# a -> f
# b -> g
# c -> h
#
# This program can both encrypt and decrypt messages.


def caesar(text, shift, encrypt=True):
    """
    Encrypt or decrypt text using the Caesar cipher.

    Parameters:
        text (str): The message to encrypt or decrypt.
        shift (int): The number of positions to shift letters.
        encrypt (bool): True for encryption, False for decryption.

    Returns:
        str: The encrypted or decrypted message.
    """

    # Make sure the shift value is an integer.
    # For example, 5 is valid, but "5" is not.
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    # The Caesar cipher uses shifts from 1 to 25.
    # A shift of 26 would return the alphabet to its
    # original position.
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    # The original lowercase alphabet.
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # When decrypting, we need to move letters in the
    # opposite direction.
    #
    # For example:
    # Encryption: a -> f  (shift +5)
    # Decryption: f -> a  (shift -5)
    if not encrypt:
        shift = -shift

    # Create the shifted alphabet.
    #
    # alphabet[shift:] gets the alphabet starting from
    # the position represented by shift.
    #
    # alphabet[:shift] gets the letters that were removed
    # from the beginning and places them at the end.
    #
    # Example with shift = 5:
    #
    # alphabet[5:]  -> fghijklmnopqrstuvwxyz
    # alphabet[:5]  -> abcde
    #
    # Result:
    # fghijklmnopqrstuvwxyzabcde
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    # Create a translation table.
    #
    # The first string contains the original lowercase
    # and uppercase alphabets.
    #
    # The second string contains the shifted lowercase
    # and uppercase alphabets.
    #
    # This allows translate() to replace every letter
    # with its corresponding shifted letter.
    translation_table = str.maketrans(
        alphabet + alphabet.upper(),
        shifted_alphabet + shifted_alphabet.upper()
    )

    # Translate the text using the translation table.
    #
    # Characters such as spaces, numbers, and punctuation
    # are not included in the table, so they remain unchanged.
    encrypted_text = text.translate(translation_table)

    # Return the resulting message.
    return encrypted_text


def encrypt(text, shift):
    """
    Encrypt a message using the Caesar cipher.

    This function calls caesar() with encrypt=True.
    """
    return caesar(text, shift)


def decrypt(text, shift):
    """
    Decrypt a message using the Caesar cipher.

    This function calls caesar() with encrypt=False.
    """
    return caesar(text, shift, encrypt=False)


# ---------------------------------------------------------
# Testing the Caesar cipher
# ---------------------------------------------------------

# This is an encrypted message.
# It was encrypted using a shift of 13.
encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'

# Print the encrypted message.
print(encrypted_text)

# Decrypt the message using a shift of 13.
decrypted_text = decrypt(encrypted_text, 13)

# Print the decrypted message.
print(decrypted_text)