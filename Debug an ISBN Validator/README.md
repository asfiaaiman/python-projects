# Debug an ISBN Validator

A beginner-friendly Python project built to practice **debugging**, **exception handling**, **functions**, **conditional statements**, **lists**, **string manipulation**, **type conversion**, **list comprehensions**, and **ISBN check-digit validation**.

The project fixes an existing ISBN validator created by Camperbot and makes it correctly validate both **ISBN-10** and **ISBN-13** codes while safely handling invalid user input.

## 📌 Project Overview

An **ISBN (International Standard Book Number)** is a unique identifier assigned to commercial books.

An ISBN can contain either:

* **10 digits** for ISBN-10
* **13 digits** for ISBN-13

The final character is a **check digit** calculated from the preceding digits.

For ISBN-10, the check digit can be:

* A number from `0` to `9`
* The uppercase letter `X`

For ISBN-13, the check digit is always a number from `0` to `9`.

This project fixes several problems in an existing ISBN validator, including:

* `IndentationError`
* `IndexError`
* `ValueError`
* `TypeError`
* An off-by-one error
* Incorrect handling of invalid ISBN characters
* Incorrect handling of user input

The program asks the user to enter an ISBN and its length in this format:

```text
ISBN,length
```

For example:

```text
1530051126,10
```

or:

```text
9781530051120,13
```

## 🛠️ Technologies Used

* **Python 3**
* Functions
* Conditional statements
* `if`, `else`
* `try` and `except`
* `ValueError`
* `IndexError`
* `TypeError`
* Lists
* List comprehensions
* String methods
* `split()`
* `isdigit()`
* `len()`
* `int()`
* `enumerate()`
* `sum()`
* Arithmetic operators
* ISBN-10 check-digit calculation
* ISBN-13 check-digit calculation

## 🚀 How It Works

### 1. Calculate the ISBN-10 Check Digit

The `calculate_check_digit_10()` function calculates the expected check digit for an ISBN-10 code.

```python
def calculate_check_digit_10(digits):
    total = sum((10 - i) * digit for i, digit in enumerate(digits))
    remainder = total % 11
    check_digit = (11 - remainder) % 11

    if check_digit == 10:
        return 'X'

    return str(check_digit)
```

The calculation logic is already provided by the lab.

The function receives the ISBN digits and returns the expected check digit as a string.

For ISBN-10, the check digit can be:

```text
0
1
2
3
4
5
6
7
8
9
X
```

The special case is handled with:

```python
if check_digit == 10:
    return 'X'
```

Therefore, a calculated value of `10` is represented by the uppercase letter `X`.

---

### 2. Calculate the ISBN-13 Check Digit

The `calculate_check_digit_13()` function calculates the expected check digit for an ISBN-13 code.

```python
def calculate_check_digit_13(digits):
    total = 0

    for i, digit in enumerate(digits):
        if i % 2 == 0:
            total += digit
        else:
            total += digit * 3

    check_digit = (10 - (total % 10)) % 10

    return str(check_digit)
```

The calculation uses alternating weights.

For each digit:

* Digits at even indexes are multiplied by `1`.
* Digits at odd indexes are multiplied by `3`.

The `%` operator is used to determine whether an index is even or odd:

```python
i % 2 == 0
```

If the remainder is `0`, the index is even.

The function finally returns the expected check digit as a string.

---

## 🔎 The `validate_isbn()` Function

The `validate_isbn()` function checks whether an ISBN is valid.

```python
def validate_isbn(isbn, length):
```

It receives:

* `isbn` → the ISBN entered by the user
* `length` → `10` or `13`

The function performs several validation steps.

---

### 1. Check the ISBN Length

The first check is:

```python
if len(isbn) != length:
    print(f'ISBN-{length} code should be {length} digits long.')
    return
```

`len()` determines how many characters are in the ISBN.

The program compares that value with the expected length.

For example:

```text
ISBN = 9781530051120
length = 10
```

The ISBN contains 13 characters, but the user specified 10.

Therefore, the program prints:

```text
ISBN-10 code should be 10 digits long.
```

Similarly, if a 10-digit ISBN is entered with length `13`, the program prints:

```text
ISBN-13 code should be 13 digits long.
```

This prevents the program from attempting to validate an ISBN using the wrong length.

---

### 2. Separate the Main Digits and Check Digit

The ISBN is divided into two parts:

```python
main_digits = isbn[0:length - 1]
given_check_digit = isbn[length - 1]
```

The first part contains all digits except the check digit.

The final character is stored separately as the given check digit.

For example, with:

```text
1530051126
```

the main digits are:

```text
153005112
```

and the check digit is:

```text
6
```

The expression:

```python
isbn[length - 1]
```

uses the correct zero-based index for the final character.

This fixes the **off-by-one error** from the original code.

---

## ⚠️ Off-by-One Error

Python uses **zero-based indexing**.

For example:

```python
isbn = '1530051126'
```

has these indexes:

```text
Index:   0 1 2 3 4 5 6 7 8 9
Character:
         1 5 3 0 0 5 1 1 2 6
```

The final character is at index:

```text
9
```

because the string has 10 characters.

The correct expression is therefore:

```python
isbn[length - 1]
```

For a length of `10`:

```python
10 - 1
```

equals:

```text
9
```

This is an important example of an **off-by-one error**, where code accidentally accesses the position immediately before or after the intended position.

---

## 🧮 Convert the Main Digits to Integers

The main digits need to be converted from strings to integers before the check-digit calculation.

The program uses:

```python
main_digits_list = [int(digit) for digit in main_digits]
```

This is a **list comprehension**.

For example:

```text
153005112
```

becomes:

```python
[1, 5, 3, 0, 0, 5, 1, 1, 2]
```

Each character is converted using:

```python
int(digit)
```

---

## 🚨 Handle Invalid ISBN Characters

An ISBN may contain invalid characters.

For example:

```text
15-0051126
```

contains a hyphen.

The conversion:

```python
int('-')
```

causes a `ValueError`.

Instead of allowing the program to crash, the conversion is placed inside a `try` block:

```python
try:
    main_digits_list = [int(digit) for digit in main_digits]
except ValueError:
    print('Invalid character was found.')
    return
```

If a character cannot be converted to an integer, Python raises a `ValueError`.

The `except` block catches the error and prints:

```text
Invalid character was found.
```

The `return` then terminates the validation function.

This is an important example of **exception handling**.

---

## 🔢 Calculate the Expected Check Digit

After the main digits have been converted successfully, the program determines which ISBN calculation should be used:

```python
if length == 10:
    expected_check_digit = calculate_check_digit_10(main_digits_list)
else:
    expected_check_digit = calculate_check_digit_13(main_digits_list)
```

If the length is `10`, the ISBN-10 calculation is used.

If the length is `13`, the ISBN-13 calculation is used.

The expected check digit is returned as a string.

---

## ✅ Compare the Check Digits

The program then compares the user's check digit with the calculated check digit:

```python
if given_check_digit == expected_check_digit:
    print('Valid ISBN Code.')
else:
    print('Invalid ISBN Code.')
```

If both values match:

```text
Valid ISBN Code.
```

is printed.

If they do not match:

```text
Invalid ISBN Code.
```

is printed.

This is the final validation step.

---

# 🖥️ The `main()` Function

The `main()` function handles the user's input.

```python
def main():
    user_input = input('Enter ISBN and length: ')
```

When the program runs, the user sees:

```text
Enter ISBN and length:
```

The user should enter the ISBN and its length separated by a comma.

For example:

```text
1530051126,10
```

---

## 1. Check for a Comma

The program first checks whether the input contains a comma:

```python
if ',' not in user_input:
    print('Enter comma-separated values.')
    return
```

The comma is required because the input contains two values:

```text
ISBN,length
```

If the user enters:

```text
1530051125
```

there is no comma.

The program prints:

```text
Enter comma-separated values.
```

and terminates.

This prevents the program from attempting to access a missing second value.

---

## 2. Split the Input

If a comma exists, the input is split:

```python
values = user_input.split(',')
```

For:

```text
1530051126,10
```

the result is approximately:

```python
['1530051126', '10']
```

The ISBN is stored in:

```python
isbn = values[0]
```

and the length is stored in:

```python
length = values[1]
```

---

## ⚠️ Handling `IndexError`

If the original program attempted to access:

```python
values[1]
```

when there was no comma-separated second value, Python could raise:

```text
IndexError
```

The corrected program checks for the comma before accessing the second element.

Therefore, input such as:

```text
1530051125
```

is handled safely.

This prevents the program from crashing because of a missing list element.

---

## 3. Validate the Length

The program checks whether the length contains only numeric characters:

```python
if not length.isdigit():
    print('Length must be a number.')
    return
```

For example:

```text
10
```

is numeric.

But:

```text
A
```

is not numeric.

If the user enters:

```text
1530051125,A
```

the program prints:

```text
Length must be a number.
```

and terminates.

---

## 4. Convert the Length to an Integer

Once the program confirms that the length contains digits, it converts it to an integer:

```python
length = int(length)
```

For example:

```text
'10'
```

becomes:

```text
10
```

This is necessary because the program later compares the length using numeric values.

---

## 5. Check Whether the Length Is 10 or 13

The program then checks:

```python
if length == 10 or length == 13:
    validate_isbn(isbn, length)
else:
    print('Length should be 10 or 13.')
```

Only two ISBN lengths are accepted:

```text
10
13
```

If the user enters:

```text
9
```

the program prints:

```text
Length should be 10 or 13.
```

---

# 🧯 Exception Handling

One of the main goals of this lab is learning how to handle errors without allowing the program to crash.

The project works with several common Python errors.

## `IndexError`

An `IndexError` can occur when trying to access a list index that does not exist.

For example:

```python
values = ['1530051125']
print(values[1])
```

There is no item at index `1`.

The corrected program prevents this situation by checking for the comma before accessing the second value.

---

## `ValueError`

A `ValueError` occurs when a value has the correct general type but cannot be converted or interpreted as expected.

For example:

```python
int('A')
```

causes a `ValueError`.

The ISBN validator handles this when converting ISBN characters:

```python
try:
    main_digits_list = [int(digit) for digit in main_digits]
except ValueError:
    print('Invalid character was found.')
    return
```

The program also checks the length before converting it to an integer.

---

## `TypeError`

The original code contained a `TypeError` caused by passing values of the wrong type to the calculation functions.

The corrected program ensures that the main ISBN digits are converted into integers:

```python
main_digits_list = [int(digit) for digit in main_digits]
```

This allows the check-digit calculation functions to perform arithmetic correctly.

---

## 🧪 Test Cases

The project can be manually tested using the following ISBN codes.

### Valid ISBN-10 Codes

```text
1530051126,10
9971502100,10
080442957X,10
```

Expected result:

```text
Valid ISBN Code.
```

### Valid ISBN-13 Codes

```text
9781530051120,13
9781947172104,13
```

Expected result:

```text
Valid ISBN Code.
```

---

## ❌ Invalid ISBN Examples

### Invalid Check Digit

Input:

```text
1530051125,10
```

Expected output:

```text
Invalid ISBN Code.
```

The ISBN has the correct length, but the supplied check digit does not match the calculated check digit.

---

### Incorrect Length

Input:

```text
9781530051120,10
```

Expected output:

```text
ISBN-10 code should be 10 digits long.
```

The ISBN contains 13 characters but the user specified length `10`.

---

### Another Incorrect Length

Input:

```text
1530051126,13
```

Expected output:

```text
ISBN-13 code should be 13 digits long.
```

The ISBN contains 10 characters but the user specified length `13`.

---

### Invalid Character

Input:

```text
15-0051126,10
```

Expected output:

```text
Invalid character was found.
```

The hyphen cannot be converted to an integer.

---

### Invalid Length Number

Input:

```text
1530051126,9
```

Expected output:

```text
Length should be 10 or 13.
```

Only `10` and `13` are accepted.

---

### Non-Numeric Length

Input:

```text
1530051125,A
```

Expected output:

```text
Length must be a number.
```

The length must be numeric.

---

### Missing Comma

Input:

```text
1530051125
```

Expected output:

```text
Enter comma-separated values.
```

The program requires the ISBN and length to be separated by a comma.

---

# 📋 Validation Results

| **ISBN Code**              | **Length**     | **Expected Message**                                                                 |
| -------------------------- | -------------- | ------------------------------------------------------------------------------------ |
| Valid                      | Valid          | `Valid ISBN Code.`                                                                   |
| Invalid check digit        | Valid          | `Invalid ISBN Code.`                                                                 |
| Wrong length               | Valid          | `ISBN-10 code should be 10 digits long.` or `ISBN-13 code should be 13 digits long.` |
| Contains invalid character | Valid          | `Invalid character was found.`                                                       |
| Any                        | Invalid number | `Length should be 10 or 13.`                                                         |
| Any                        | Non-numeric    | `Length must be a number.`                                                           |
| Not comma-separated        | Not applicable | `Enter comma-separated values.`                                                      |

---

# 🧠 Concepts Practiced

This project reinforces the following Python concepts:

| **Concept**            | **Example**                             |
| ---------------------- | --------------------------------------- |
| Functions              | `validate_isbn()`                       |
| Function parameters    | `isbn, length`                          |
| Conditional statements | `if`, `else`                            |
| Exception handling     | `try`, `except`                         |
| `ValueError`           | `int('A')`                              |
| `IndexError`           | Accessing a missing list element        |
| Type conversion        | `int(length)`                           |
| String splitting       | `user_input.split(',')`                 |
| String checking        | `length.isdigit()`                      |
| String length          | `len(isbn)`                             |
| Lists                  | `main_digits_list`                      |
| List comprehensions    | `[int(digit) for digit in main_digits]` |
| `enumerate()`          | Looping through ISBN digits             |
| `sum()`                | Calculating weighted totals             |
| Modulo operator        | `%`                                     |
| Comparison operators   | `length == 10`                          |
| Logical operators      | `length == 10 or length == 13`          |
| Early return           | `return`                                |
| Debugging              | Fixing existing errors                  |
| Off-by-one errors      | `length - 1`                            |
| ISBN-10 validation     | `calculate_check_digit_10()`            |
| ISBN-13 validation     | `calculate_check_digit_13()`            |

---

# 🧩 Debugging Fixes

The original code contained several problems that needed to be identified and fixed.

The lab focuses on fixing:

* **IndentationError**
* **IndexError**
* **ValueError**
* **TypeError**
* **Off-by-one error**
* Incorrect handling of invalid characters
* Incorrect input handling

The goal is not simply to rewrite the program, but to understand why the existing code fails and make the smallest necessary corrections.

Debugging is basically detective work, except the suspect is your own code and it refuses to confess.

---

# 🧪 FreeCodeCamp Tests

The project includes automated tests that verify:

* Required functions exist.
* The `main()` function exists.
* Invalid input does not crash the program.
* Missing comma input is handled correctly.
* Non-numeric length input is handled correctly.
* Invalid ISBN characters are handled correctly.
* Valid ISBN-10 codes are accepted.
* Valid ISBN-13 codes are accepted.
* Invalid check digits are rejected.
* Incorrect ISBN lengths are rejected.
* Unsupported lengths are rejected.
* ISBN-10 codes ending in `X` are accepted.

There are **20 tests** covering the required behavior.

---

# ⚠️ Important: Comment Out `main()`

The lab specifically requires the call to `main()` in the global space to be commented out:

```python
# main()
```

This is important because the FreeCodeCamp tests need to import and test the functions without the program immediately asking for user input.

The function itself should still exist:

```python
def main():
    ...
```

Only the direct call should be commented out:

```python
# main()
```

This allows the automated tests to run correctly.

---

# ▶️ How to Run

Make sure **Python 3** is installed on your computer.

Save the program in a Python file:

```text
isbn_validator.py
```

Then run:

```bash
python isbn_validator.py
```

On systems where Python 3 is accessed using `python3`, run:

```bash
python3 isbn_validator.py
```

When running the program manually, the prompt will be:

```text
Enter ISBN and length:
```

Enter an ISBN and its length in comma-separated format.

For example:

```text
1530051126,10
```

---

# 🎯 Learning Goal

The main goal of this project is to develop practical **Python debugging and error-handling skills**.

The exercise demonstrates how to:

* Identify and fix syntax and indentation problems.
* Handle `IndexError` safely.
* Handle `ValueError` safely.
* Prevent `TypeError` by using the correct data types.
* Fix off-by-one errors.
* Validate user input.
* Work with strings and lists.
* Use list comprehensions.
* Convert strings to integers.
* Use functions to organize code.
* Validate data using calculated check digits.

These skills provide a foundation for more advanced Python topics such as **file processing, APIs, data validation, testing, automation, data engineering, and machine learning**.

## 📖 Source

This project was completed as part of the **freeCodeCamp Python v9 Debug an ISBN Validator lab**.

## 👩‍💻 Author

**Asfia Aiman**

Part of my Python learning journey with **freeCodeCamp**.
