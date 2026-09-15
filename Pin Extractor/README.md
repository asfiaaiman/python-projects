# Pin Extractor

A beginner-friendly Python project built to practice the fundamentals of **functions**, **lists**, **loops**, **string manipulation**, **string splitting**, **enumeration**, **conditional statements**, **type conversion**, and **indexing**.

The project extracts secret PIN codes from poems by using the length of specific words from each line.

## 📌 Project Overview

This project demonstrates how Python can process multiple pieces of text and extract information from them using loops and string operations.

The `pin_extractor()` function takes a list of poems and generates a secret numeric code for each poem.

It uses:

* Lines from each poem
* Words from each line
* The current line index
* Word length
* `0` when a required word does not exist
* A list to store the generated secret codes

## 🛠️ Technologies Used

* **Python 3**
* Functions
* Lists
* `for` loops
* `enumerate()`
* String splitting with `split()`
* String concatenation
* `len()`
* Conditional statements
* Type conversion using `str()`

## 🚀 How It Works

### 1. Create the Pin Extractor Function

The project starts with a function named `pin_extractor()`:

```python
def pin_extractor(poems):
```

The function accepts `poems`, which contains multiple poems.

A list is created to store the generated secret codes:

```python
secret_codes = []
```

Each poem will produce one secret code.

### 2. Loop Through the Poems

The program uses a `for` loop to process each poem:

```python
for poem in poems:
```

This means the function processes every poem in the provided list one at a time.

For example:

```python
poems = [poem, poem2, poem3]
```

The loop processes:

1. `poem`
2. `poem2`
3. `poem3`

### 3. Create an Empty Secret Code

For every poem, an empty string is created:

```python
secret_code = ''
```

The extracted numbers will be added to this string as the poem is processed.

For example, if the extracted values are:

```text
4
2
5
1
```

they are added together to create:

```text
4251
```

### 4. Split the Poem into Lines

Each poem is divided into individual lines using `split('\n')`:

```python
lines = poem.split('\n')
```

For example:

```python
poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""
```

becomes:

```text
Stars and the moon
shine in the sky
white and
until the end of the night
```

Each line is stored as an item in the `lines` list.

### 5. Loop Through Each Line

The program uses `enumerate()` to process every line while also keeping track of its index:

```python
for line_index, line in enumerate(lines):
```

`enumerate()` provides two values:

* `line_index` - the position of the line
* `line` - the actual line of text

For example:

```text
Line index 0 → Stars and the moon
Line index 1 → shine in the sky
Line index 2 → white and
Line index 3 → until the end of the night
```

The index is important because it determines which word should be used from each line.

### 6. Split Each Line into Words

Each line is split into individual words:

```python
words = line.split()
```

For example:

```text
Stars and the moon
```

becomes:

```python
['Stars', 'and', 'the', 'moon']
```

The program can then access individual words using their indexes.

### 7. Select the Word Based on the Line Index

The program checks whether the current line contains a word at the current line index:

```python
if len(words) > line_index:
```

This prevents the program from trying to access a word that does not exist.

For example, if:

```python
line_index = 2
```

the program needs the word at index `2`.

For:

```text
white and
```

the words are:

```python
['white', 'and']
```

There are only two words, so index `2` does not exist.

Therefore, the program uses the fallback value `0`.

### 8. Extract the Word Length

When the required word exists, its length is added to the secret code:

```python
secret_code += str(len(words[line_index]))
```

For example:

```text
Stars and the moon
```

At line index `0`, the program selects:

```text
Stars
```

The word contains 5 characters.

Therefore:

```python
len('Stars')
```

produces:

```text
5
```

The number is converted to a string using:

```python
str()
```

and added to the secret code.

### 9. Add Zero When a Word Does Not Exist

If the required word does not exist, the program adds `0`:

```python
else:
    secret_code += '0'
```

This allows the function to continue processing the poem instead of producing an indexing error.

For example:

```text
white and
```

contains only two words:

```text
index 0 → white
index 1 → and
```

There is no word at index `2`, so:

```text
0
```

is added to the secret code.

### 10. Store the Secret Code

After processing all lines in a poem, the generated code is added to the `secret_codes` list:

```python
secret_codes.append(secret_code)
```

If three poems generate:

```text
5026
5736
4110
```

the list becomes:

```python
['5026', '5736', '4110']
```

### 11. Return the Secret Codes

After all poems have been processed, the function returns the list:

```python
return secret_codes
```

This is important because without the `return` statement, the function would finish its work but return `None`.

The completed function should therefore end with:

```python
secret_codes.append(secret_code)

return secret_codes
```

## 🔐 PIN Extraction Logic

The important part of the algorithm is:

```python
for line_index, line in enumerate(lines):
    words = line.split()

    if len(words) > line_index:
        secret_code += str(len(words[line_index]))
    else:
        secret_code += '0'
```

The process can be summarized as:

```text
Poem
  ↓
Split into lines
  ↓
Get line index
  ↓
Split line into words
  ↓
Use line index as word index
  ↓
Find word length
  ↓
Add length to secret code
  ↓
If word doesn't exist → add 0
```

## 📝 Example Poem

The first poem is:

```python
poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""
```

The lines and selected words are:

| **Line Index** | **Line**                     | **Selected Word** | **Length** |
| -------------- | ---------------------------- | ----------------- | ---------- |
| `0`            | `Stars and the moon`         | `Stars`           | `5`        |
| `1`            | `shine in the sky`           | `in`              | `2`        |
| `2`            | `white and`                  | No word           | `0`        |
| `3`            | `until the end of the night` | `the`             | `3`        |

Therefore, the extracted PIN is:

```text
5203
```

The important detail is that the program uses the **line index as the word index**.

## 📖 Example Poems

The project contains three example poems:

```python
poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'

poem3 = 'There\nonce\nwas\na\ndragon'
```

They can be passed to the function as a list:

```python
print(pin_extractor([poem, poem2, poem3]))
```

The function then processes each poem and returns a list containing the generated PIN for each one.

## 📤 Expected Output

Using:

```python
print(pin_extractor([poem, poem2, poem3]))
```

the expected output is:

```text
['5203', '3566', '5110']
```

Each string represents the PIN extracted from one poem.

## 📚 Concepts Practiced

This project reinforces the following Python concepts:

| **Concept**            | **Example**                        |
| ---------------------- | ---------------------------------- |
| Functions              | `def pin_extractor(poems):`        |
| Lists                  | `secret_codes = []`                |
| `for` loops            | `for poem in poems:`               |
| `enumerate()`          | `enumerate(lines)`                 |
| String splitting       | `poem.split('\n')`                 |
| Word splitting         | `line.split()`                     |
| String indexing        | `words[line_index]`                |
| String length          | `len(words[line_index])`           |
| String concatenation   | `secret_code += ...`               |
| Type conversion        | `str(len(...))`                    |
| Conditional statements | `if len(words) > line_index:`      |
| `else` statement       | `else:`                            |
| List methods           | `secret_codes.append(secret_code)` |
| `return` statement     | `return secret_codes`              |

## ▶️ How to Run

Make sure **Python 3** is installed on your computer.

Save the program in a Python file:

```text
index.py
```

Then run:

```bash
python index.py
```

On systems where Python 3 is accessed using `python3`, run:

```bash
python3 index.py
```

To test all three example poems, use:

```python
print(pin_extractor([poem, poem2, poem3]))
```

## 🎯 Learning Goal

The main goal of this project is to build a strong foundation in Python **loops, lists, strings, and indexing**.

The exercise demonstrates how Python can process multiple pieces of text, break them into smaller parts, access specific elements using indexes, calculate string lengths, and combine the results into useful information.

These concepts provide a foundation for more advanced Python topics such as **list comprehensions, dictionaries, file processing, data extraction, regular expressions, and text analysis**.

## 👩‍💻 Author

**Asfia Aiman**

Part of my Python learning journey with **freeCodeCamp**.
