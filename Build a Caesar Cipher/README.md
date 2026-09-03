# Caesar Cipher

[svg](https://github.com/asfiaaiman/python-projects/tree/main/Caesar%20Cipher#caesar-cipher)

A beginner-friendly Python project that implements a **Caesar cipher** to encrypt and decrypt messages by shifting letters in the alphabet by a fixed number of positions.

This project was created to practice **strings, string slicing, variables, functions, parameters, conditional statements, type checking, string methods, and character translation in Python**.

## 📌 Problem

[svg](https://github.com/asfiaaiman/python-projects/tree/main/Caesar%20Cipher#-problem)

Build a Caesar cipher that can encrypt and decrypt text using a specified shift value.

The program should:

1. Create an alphabet containing lowercase letters.
2. Create a shifted version of the alphabet.
3. Create a translation table using `str.maketrans()`.
4. Encrypt a message using `translate()`.
5. Support uppercase letters.
6. Decrypt an encrypted message.
7. Validate that the shift is an integer between 1 and 25.

## 🛠️ Technologies Used

[svg](https://github.com/asfiaaiman/python-projects/tree/main/Caesar%20Cipher#%EF%B8%8F-technologies-used)

* **Python 3**
* Variables
* Strings
* String slicing
* String concatenation
* Functions
* Function parameters
* `if` statements
* `isinstance()`
* `upper()` method
* `str.maketrans()`
* `translate()` method
* Boolean values
* `return` statements

## 🚀 How It Works

[svg](https://github.com/asfiaaiman/python-projects/tree/main/Caesar%20Cipher#-how-it-works)

### 1. Create the Caesar Function

[svg](https://github.com/asfiaaiman/python-projects/tree/main/Caesar%20Cipher#1-create-the-caesar-function)

The main function is created with three parameters:

```python
def caesar(text, shift, encrypt=True):
```

**svg**

The parameters are:

* `text` - The message to encrypt or decrypt.
* `shift` - The number of positions to shift each letter.
* `encrypt` - Determines whether the function should encrypt or decrypt the message.

**svg**

The `encrypt` parameter defaults to `True`, so the function performs encryption unless told otherwise.

### 2. Validate the Shift

[svg](https://github.com/asfiaaiman/python-projects/tree/main/Caesar%20Cipher#2-validate-the-shift)

The program first checks whether the shift is an integer:

```python
if not isinstance(shift, int):
    return 'Shift must be an integer value.'
```

**svg**

The `isinstance()` function checks whether `shift` is an integer.

For example:

```python
isinstance(5, int)
```

returns:

```text
True
```

**svg**

The program then checks whether the shift is between 1 and 25:

```python
if shift < 1 or shift > 25:
    return 'Shift must be an integer between 1 and 25.'
```

**svg**

A shift of `26` would produce the original alphabet again, so the program only accepts values from **1 to 25**.

### 3. Create the Alphabet

[svg](https://github.com/asfiaaiman/python-projects/tree/main/Caesar%20Cipher#3-create-the-alphabet)

The lowercase alphabet is stored in a variable:

```python
alphabet = 'abcdefghijklmnopqrstuvwxyz'
```

**svg**

The alphabet contains 26 letters:

```text
abcdefghijklmnopqrstuvwxyz
```

**svg**

Python uses zero-based indexing, so the letter `a` is at index `0`, while `f` is at index `5`.

### 4. Handle Decryption

[svg](https://github.com/asfiaaiman/python-projects/tree/main/Caesar%20Cipher#4-handle-decryption)

When encrypting, letters are shifted forward.

When decrypting, letters need to be shifted in the opposite direction.

The program changes the shift to a negative value when `encrypt` is `False`:

```python
if not encrypt:
    shift = -shift
```

**svg**

For example, a shift of:

```text
5
```

becomes:

```text
-5
```

**svg**

This allows the same `caesar()` function to handle both encryption and decryption.

### 5. Create the Shifted Alphabet

[svg](https://github.com/asfiaaiman/python-projects/tree/main/Caesar%20Cipher#5-create-the-shifted-alphabet)

The shifted alphabet is created using string slicing:

```python
shifted_alphabet = alphabet[shift:] + alphabet[:shift]
```

**svg**

With a shift of `5`:

```python
alphabet[5:]
```

produces:

```text
fghijklmnopqrstuvwxyz
```

**svg**

The first five letters are extracted using:

```python
alphabet[:5]
```

which produces:

```text
abcde
```

**svg**

The two parts are then combined:

```text
fghijklmnopqrstuvwxyzabcde
```

**svg**

The resulting shifted alphabet maps each original letter to its encrypted equivalent:

```text
Original: abcdefghijklmnopqrstuvwxyz
Shifted:  fghijklmnopqrstuvwxyzabcde
```

### 6. Create the Translation Table

[svg](https://github.com/asfiaaiman/python-projects/tree/main/Caesar%20Cipher#6-create-the-translation-table)

Python's `str.maketrans()` method is used to create a translation table:

```python
translation_table = str.maketrans(
    alphabet + alphabet.upper(),
    shifted_alphabet + shifted_alphabet.upper()
)
```

**svg**

The first argument contains the original lowercase and uppercase alphabets:

```text
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
```

**svg**

The second argument contains the shifted lowercase and uppercase alphabets:

```text
fghijklmnopqrstuvwxyzabcde
FGHIJKLMNOPQRSTUVWXYZABCDE
```

**svg**

This allows the program to encrypt both lowercase and uppercase characters.

### 7. Encrypt the Text

[svg](https://github.com/asfiaaiman/python-projects/tree/main/Caesar%20Cipher#7-encrypt-the-text)

The `translate()` method is used with the translation table:

```python
encrypted_text = text.translate(translation_table)
```

**svg**

For example, with a shift of `5`:

```text
hello
```

becomes:

```text
mjqqt
```

**svg**

Characters that are not included in the translation table remain unchanged.

For example:

```text
Hello, World! 123
```

becomes:

```text
Mjqqt, Btwqi! 123
```

**svg**

Spaces, punctuation, and numbers are not modified.

### 8. Create the Encrypt Function

[svg](https://github.com/asfiaaiman/python-projects/tree/main/Caesar%20Cipher#8-create-the-encrypt-function)

A separate `encrypt()` function is created to make encryption easier to use:

```python
def encrypt(text, shift):
    return caesar(text, shift)
```

**svg**

For example:

```python
encrypt('hello', 5)
```

produces:

```text
mjqqt
```

### 9. Create the Decrypt Function

[svg](https://github.com/asfiaaiman/python-projects/tree/main/Caesar%20Cipher#9-create-the-decrypt-function)

A separate `decrypt()` function is created for decryption:

```python
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)
```

**svg**

For example:

```python
decrypt('mjqqt', 5)
```

produces:

```text
hello
```

**svg**

The function passes `encrypt=False` to the main `caesar()` function, which causes the shift to become negative.

## 📤 Expected Output

[svg](https://github.com/asfiaaiman/python-projects/tree/main/Caesar%20Cipher#-expected-output)

The program uses the following encrypted message:

```python
encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'
```

**svg**

The message is decrypted using a shift of `13`:

```python
decrypted_text = decrypt(encrypted_text, 13)
```

**svg**

The expected output is:

```text
Pbhentr vf sbhaq va hayvxryl cynprf.
Courage is found in unlikely places.
```

**svg**

The first line is the encrypted message, while the second line is the decrypted message.

## 📚 Concepts Practiced

[svg](https://github.com/asfiaaiman/python-projects/tree/main/Caesar%20Cipher#-concepts-practiced)

| **Concept**            | **Example**                               |
| ---------------------- | ----------------------------------------- |
| Variables              | `alphabet = 'abcdefghijklmnopqrstuvwxyz'` |
| Strings                | `'hello world'`                           |
| String slicing         | `alphabet[shift:]`                        |
| String slicing         | `alphabet[:shift]`                        |
| String concatenation   | `alphabet[shift:] + alphabet[:shift]`     |
| Functions              | `def caesar(text, shift, encrypt=True)`   |
| Function parameters    | `text`, `shift`, `encrypt`                |
| Conditional statements | `if not encrypt:`                         |
| Type checking          | `isinstance(shift, int)`                  |
| Boolean values         | `True`, `False`                           |
| Uppercase conversion   | `alphabet.upper()`                        |
| Translation table      | `str.maketrans()`                         |
| String translation     | `text.translate(translation_table)`       |
| Return values          | `return encrypted_text`                   |
| Output                 | `print()`                                 |

## ▶️ How to Run

[svg](https://github.com/asfiaaiman/python-projects/tree/main/Caesar%20Cipher#%EF%B8%8F-how-to-run)

Make sure Python 3 is installed.

Run the following command from the project directory:

```bash
python index.py
```

**svg**

On systems where Python is accessed using `python3`, run:

```bash
python3 index.py
```

**svg**

The program will display the encrypted message followed by the decrypted message.

## 🔒 Limitations

[svg](https://github.com/asfiaaiman/python-projects/tree/main/Caesar%20Cipher#-limitations)

The Caesar cipher is a simple encryption technique and is **not secure for protecting sensitive information**.

There are only 25 possible shifts, meaning an attacker can easily try every possible shift to discover the original message.

**svg**

This project is intended for **educational purposes** and should not be used for:

* Password protection
* Secure communication
* Storing sensitive information
* Protecting confidential data
* Production-level encryption

## 🎯 Learning Goal

[svg](https://github.com/asfiaaiman/python-projects/tree/main/Caesar%20Cipher#-learning-goal)

The goal of this project is to strengthen the fundamentals of working with **strings, functions, slicing, conditionals, and built-in Python methods** by implementing a simple encryption and decryption algorithm.

The project also provides an introduction to the basic idea of **substitution ciphers** and how characters can be mapped from one alphabet to another.

## 👩‍💻 Author

[svg](https://github.com/asfiaaiman/python-projects/tree/main/Caesar%20Cipher#-author)

**Asfia Aiman**

Part of my Python learning journey with **freeCodeCamp**.
