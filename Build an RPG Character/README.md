# RPG Character Builder

A beginner-friendly Python project built to practice the fundamentals of **functions**, **function parameters**, **conditional statements**, **type checking**, **string manipulation**, **arithmetic operations**, and **string multiplication**.

The project creates an RPG character by validating the character's name and distributing exactly 7 points across three character stats: Strength, Intelligence, and Charisma.

## 📌 Project Overview

This project demonstrates how Python functions can be used to validate user data and generate formatted output.

It creates:

* An RPG character name
* Strength (STR) statistics
* Intelligence (INT) statistics
* Charisma (CHA) statistics
* Validation rules for the character name
* Validation rules for character statistics
* A visual stat bar using full and empty dots
* A character with exactly 7 starting points

## 🛠️ Technologies Used

* **Python 3**
* Functions
* Function parameters
* Conditional statements
* `isinstance()`
* String manipulation
* String multiplication
* Arithmetic operations
* String concatenation

## 🚀 How It Works

### 1. Create the Character Function

The project starts with a function named `create_character()`.

The function accepts four parameters:

```python
def create_character(name, strength, intelligence, charisma):
```

These parameters represent:

* `name` - Character name
* `strength` - Strength stat
* `intelligence` - Intelligence stat
* `charisma` - Charisma stat

The function validates all of these values before creating the character.

### 2. Validate the Character Name

The first validation checks whether the character name is a string.

```python
if not isinstance(name, str):
    return 'The character name should be a string'
```

For example:

```python
create_character(123, 4, 2, 1)
```

Output:

```text
The character name should be a string
```

### 3. Check for an Empty Name

The character must have a name.

An empty string is checked using:

```python
if name == '':
    return 'The character should have a name'
```

For example:

```python
create_character('', 4, 2, 1)
```

Output:

```text
The character should have a name
```

### 4. Check the Name Length

The character name cannot contain more than 10 characters.

Python's `len()` function is used to determine the length:

```python
if len(name) > 10:
    return 'The character name is too long'
```

For example:

```python
create_character('Christopher', 4, 2, 1)
```

Output:

```text
The character name is too long
```

### 5. Check for Spaces

Character names cannot contain spaces.

The `in` operator is used to check whether the name contains a space:

```python
if ' ' in name:
    return 'The character name should not contain spaces'
```

For example:

```python
create_character('Dark Knight', 4, 2, 1)
```

Output:

```text
The character name should not contain spaces
```

A name such as:

```python
create_character('DarkKnight', 4, 2, 1)
```

passes this validation.

## ⚔️ Character Stat Validation

The character has three statistics:

* **STR** - Strength
* **INT** - Intelligence
* **CHA** - Charisma

Each statistic must follow specific rules.

### 1. Stats Must Be Integers

All three stats must be integers.

The `isinstance()` function is used to check their types:

```python
if (
    not isinstance(strength, int)
    or not isinstance(intelligence, int)
    or not isinstance(charisma, int)
):
    return 'All stats should be integers'
```

For example:

```python
create_character('ren', '4', 2, 1)
```

Output:

```text
All stats should be integers
```

The value `'4'` is a string, not an integer.

### 2. Stats Must Be at Least 1

Every stat must have a minimum value of `1`.

```python
if strength < 1 or intelligence < 1 or charisma < 1:
    return 'All stats should be no less than 1'
```

For example:

```python
create_character('ren', 0, 3, 4)
```

Output:

```text
All stats should be no less than 1
```

### 3. Stats Cannot Be Greater Than 4

Every stat has a maximum value of `4`.

```python
if strength > 4 or intelligence > 4 or charisma > 4:
    return 'All stats should be no more than 4'
```

For example:

```python
create_character('ren', 5, 1, 1)
```

Output:

```text
All stats should be no more than 4
```

### 4. Stats Must Total 7 Points

The character starts with exactly **7 points**.

The three statistics are added together:

```python
if strength + intelligence + charisma != 7:
    return 'The character should start with 7 points'
```

For example:

```python
strength = 4
intelligence = 2
charisma = 1
```

The total is:

```text
4 + 2 + 1 = 7
```

Therefore, the character is valid.

However:

```python
create_character('ren', 4, 4, 1)
```

is invalid because:

```text
4 + 4 + 1 = 9
```

Output:

```text
The character should start with 7 points
```

## ⭐ Generate Character Stat Bars

Once all values pass validation, the program creates visual stat bars using two characters:

```python
full_dot = '●'
empty_dot = '○'
```

A full dot represents an assigned stat point, while an empty dot represents an unused point.

For example:

```python
full_dot * 4
```

produces:

```text
●●●●
```

And:

```python
empty_dot * 6
```

produces:

```text
○○○○○○
```

They can be combined to create a 10-dot stat bar:

```python
full_dot * 4 + empty_dot * 6
```

Output:

```text
●●●●○○○○○○
```

The number of empty dots is calculated using:

```python
10 - strength
```

Therefore, a strength value of `4` produces:

```text
STR ●●●●○○○○○○
```

## 🧙 Create the Final Character

After all validation checks pass, the function returns the character name and all three stat bars.

For example:

```python
create_character('ren', 4, 2, 1)
```

Output:

```text
ren
STR ●●●●○○○○○○
INT ●●○○○○○○○○
CHA ●○○○○○○○○○
```

The character has:

* Strength: 4
* Intelligence: 2
* Charisma: 1
* Total points: 7

## 📚 Concepts Practiced

This project reinforces the following Python concepts:

| **Concept**            | **Example**                              |
| ---------------------- | ---------------------------------------- |
| Functions              | `def create_character(...):`             |
| Function parameters    | `name, strength, intelligence, charisma` |
| Conditional statements | `if len(name) > 10:`                     |
| Type checking          | `isinstance(name, str)`                  |
| String checking        | `' ' in name`                            |
| String multiplication  | `full_dot * strength`                    |
| Arithmetic operations  | `strength + intelligence + charisma`     |
| String concatenation   | `name + '\nSTR ' + strength_bar`         |
| Boolean operators      | `or`                                     |
| `return` statements    | `return 'Error message'`                 |
| `len()`                | `len(name)`                              |
| Newline characters     | `'\n'`                                   |

## ⚠️ Python Naming Note

The exercise specifically mentions that `str` and `int` should not be used as variable names.

Although `str` and `int` may look like suitable abbreviations for **Strength** and **Intelligence**, they are already built-in Python names.

For example:

```python
str()
```

is used for string conversion, while:

```python
int()
```

is used for integer conversion.

Therefore, this project uses descriptive names:

```python
strength
intelligence
charisma
```

instead of:

```python
str
int
cha
```

This keeps the code readable and avoids accidentally overwriting Python's built-in functionality.

## ▶️ How to Run

Make sure **Python 3** is installed on your computer.

Save the code in a Python file:

```text
index.py
```

Then run:

```bash
python index.py
```

On systems where Python 3 is accessed through `python3`, use:

```bash
python3 index.py
```

## 📤 Expected Output

When the program runs with:

```python
print(create_character('ren', 4, 2, 1))
```

the expected output is:

```text
ren
STR ●●●●○○○○○○
INT ●●○○○○○○○○
CHA ●○○○○○○○○○
```

## 🎯 Learning Goal

The main goal of this project is to build a strong foundation in Python **functions and data validation**.

The exercise helps develop an understanding of how functions receive data, validate different types of values, apply multiple conditions, perform calculations, and return formatted strings.

These concepts provide a foundation for more advanced Python topics such as **lists, dictionaries, loops, modules, error handling, and object-oriented programming**.

## 👩‍💻 Author

**Asfia Aiman**

Built as part of my Python learning journey with **freeCodeCamp**.
