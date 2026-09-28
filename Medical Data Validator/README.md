# Medical Data Validator

A beginner-friendly Python project built to practice the fundamentals of **data validation**, **Boolean values**, **conditional statements**, **dictionaries**, **lists**, **functions**, **type checking**, **list comprehensions**, and **regular expressions**.

The project validates a collection of medical records and checks whether each record follows the required structure and data rules.

## 📌 Project Overview

This project demonstrates how Python can validate structured data by checking both the **format of the data** and the **values stored inside it**.

It checks:

* Whether the input is a list or tuple
* Whether each record is a dictionary
* Whether each dictionary contains the required keys
* Whether the patient ID follows the correct format
* Whether the patient's age is valid
* Whether the gender is valid
* Whether the diagnosis is a string or `None`
* Whether medications are stored in a list
* Whether every medication is a string
* Whether the last visit ID follows the correct format

## 🛠️ Technologies Used

* **Python 3**
* Regular expressions
* `re.fullmatch()`
* `re.IGNORECASE`
* Dictionaries
* Lists
* Tuples
* Functions
* Boolean values
* `isinstance()`
* `if`, `continue`, and `return`
* List comprehensions
* `enumerate()`
* Dictionary unpacking with `**`
* `print()` function

## 🚀 How It Works

### 1. Define the Medical Records

The program starts with a list containing multiple medical records:

```python
medical_records = [
    {
        'patient_id': 'P1001',
        'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301',
    }
]
```

Each medical record is represented as a **dictionary**.

Each dictionary contains:

* `patient_id`
* `age`
* `gender`
* `diagnosis`
* `medications`
* `last_visit_id`

The complete collection of records is stored inside a **list**.

---

### 2. Validate Individual Records

The `find_invalid_records()` function is responsible for checking the individual fields of one medical record:

```python
def find_invalid_records(
    patient_id, age, gender, diagnosis, medications, last_visit_id
):
```

The function receives all six expected values as parameters.

It then creates a dictionary called `constraints` containing the validation result for every field.

```python
constraints = {
    'patient_id': ...,
    'age': ...,
    'gender': ...,
    'diagnosis': ...,
    'medications': ...,
    'last_visit_id': ...
}
```

Each validation expression produces a Boolean value:

```text
True
```

if the value is valid, or:

```text
False
```

if the value is invalid.

---

### 3. Validate the Patient ID

The patient ID must be:

* A string
* A lowercase or uppercase `p`
* Followed by one or more digits

The validation is:

```python
isinstance(patient_id, str)
and re.fullmatch('p\d+', patient_id, re.IGNORECASE)
```

For example:

```text
P1001
p1002
P12345
```

are valid formats.

The regular expression:

```python
p\d+
```

means:

* `p` → match the letter `p`
* `\d` → match a digit
* `+` → match one or more digits

`re.IGNORECASE` allows both uppercase and lowercase `p`.

Therefore:

```text
P1001
```

and:

```text
p1001
```

are both accepted.

---

### 4. Validate the Age

The patient's age must be an integer and must be at least 18:

```python
isinstance(age, int) and age >= 18
```

The first condition:

```python
isinstance(age, int)
```

checks whether the value is an integer.

The second condition:

```python
age >= 18
```

checks whether the age is at least 18.

Both conditions must be true because the program uses the `and` operator.

For example:

```python
age = 34
```

produces:

```text
True
```

while:

```python
age = 16
```

produces:

```text
False
```

---

### 5. Validate the Gender

The gender must be a string containing either:

```text
male
```

or:

```text
female
```

The validation is:

```python
isinstance(gender, str) and gender.lower() in ('male', 'female')
```

The `.lower()` method converts the value to lowercase.

Therefore:

```text
Male
MALE
male
```

are treated the same way.

The `in` operator checks whether the resulting value exists in:

```python
('male', 'female')
```

For example:

```python
gender = 'Female'
```

becomes:

```text
female
```

after `.lower()`.

The value exists in the allowed options, so the result is:

```text
True
```

---

### 6. Validate the Diagnosis

The diagnosis can either be a string or `None`:

```python
isinstance(diagnosis, str) or diagnosis is None
```

The `or` operator means that either condition can be true.

For example:

```python
diagnosis = 'Asthma'
```

is valid because it is a string.

This is also valid:

```python
diagnosis = None
```

This allows a medical record to exist even when no diagnosis has been provided.

---

### 7. Validate Medications

The medications value must be a list:

```python
isinstance(medications, list)
```

The program also checks that every item inside the list is a string:

```python
all([isinstance(i, str) for i in medications])
```

For example:

```python
medications = ['Metformin', 'Insulin']
```

is valid because both items are strings.

The `all()` function returns `True` only when every condition inside the generated list is true.

For example:

```python
[True, True]
```

results in:

```text
True
```

But:

```python
[True, False]
```

results in:

```text
False
```

This ensures that the medications list does not contain unexpected data types.

---

### 8. Validate the Last Visit ID

The last visit ID must:

* Be a string
* Start with `v`
* Be followed by one or more digits

The validation is:

```python
isinstance(last_visit_id, str)
and re.fullmatch('v\d+', last_visit_id, re.IGNORECASE)
```

Examples of valid formats include:

```text
V2301
v2302
V12345
```

The regular expression:

```python
v\d+
```

works similarly to the patient ID pattern.

`re.IGNORECASE` allows both:

```text
V
```

and:

```text
v
```

---

### 9. Find Invalid Fields

After validating every field, the program returns the names of fields that failed validation:

```python
return [key for key, value in constraints.items() if not value]
```

This is a **list comprehension**.

It loops through:

```python
constraints.items()
```

which provides both the field name and its validation result.

For example, if:

```python
constraints = {
    'patient_id': True,
    'age': False,
    'gender': True
}
```

the result will be:

```python
['age']
```

The condition:

```python
if not value
```

selects only fields whose validation result is `False`.

Python once again turns something that looks complicated into one line, presumably to make beginners suspicious of themselves.

---

## 🔍 The `validate()` Function

The `validate()` function checks the overall structure of the medical records.

```python
def validate(data):
```

It performs several validation steps.

### 1. Check the Input Type

The program first checks whether the supplied data is a list or tuple:

```python
is_sequence = isinstance(data, (list, tuple))
```

A tuple is included because the validator accepts either:

```python
list
```

or:

```python
tuple
```

If the input is neither, the function prints an error:

```python
if not is_sequence:
    print('Invalid format: expected a list or tuple.')
    return False
```

The function immediately returns `False` because the entire input has an invalid structure.

---

### 2. Track Invalid Data

The program creates a Boolean variable:

```python
is_invalid = False
```

This keeps track of whether any problem is found while validating the records.

Initially:

```text
False
```

means that no invalid data has been found yet.

If an error is discovered, it changes to:

```python
is_invalid = True
```

---

### 3. Define the Required Keys

Every medical record must contain exactly these keys:

```python
key_set = set(
    ['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id']
)
```

A `set` is used because the program is interested in comparing the collection of keys rather than their order.

The expected keys are:

```text
patient_id
age
gender
diagnosis
medications
last_visit_id
```

---

### 4. Loop Through the Records

The program uses `enumerate()`:

```python
for index, dictionary in enumerate(data):
```

`enumerate()` provides two values:

* `index` → position of the record
* `dictionary` → actual medical record

For example:

```text
index = 0
```

refers to the first record.

```text
index = 1
```

refers to the second record.

This makes it possible to report exactly where an invalid record was found.

---

### 5. Check That Each Record Is a Dictionary

Each item must be a dictionary:

```python
if not isinstance(dictionary, dict):
    print(f'Invalid format: expected a dictionary at position {index}.')
    is_invalid = True
    continue
```

If the item is not a dictionary:

1. An error message is printed.
2. `is_invalid` becomes `True`.
3. `continue` skips the current item.
4. The loop moves to the next record.

---

### 6. Check the Dictionary Keys

The program compares the dictionary's keys against the required keys:

```python
if set(dictionary.keys()) != key_set:
```

This detects:

* Missing keys
* Extra keys
* Incorrect key names

For example, this is invalid:

```python
{
    'patient_id': 'P1001',
    'age': 34,
    'gender': 'Female'
}
```

because several required keys are missing.

The program reports the invalid position and continues checking the remaining records.

---

### 7. Validate the Field Values

Once the structure is valid, the dictionary is passed to:

```python
find_invalid_records(**dictionary)
```

The `**` operator **unpacks the dictionary**.

For example:

```python
dictionary = {
    'patient_id': 'P1001',
    'age': 34,
    'gender': 'Female',
    'diagnosis': 'Asthma',
    'medications': ['Albuterol'],
    'last_visit_id': 'V2303'
}
```

Using:

```python
find_invalid_records(**dictionary)
```

is equivalent to passing:

```python
find_invalid_records(
    patient_id='P1001',
    age=34,
    gender='Female',
    diagnosis='Asthma',
    medications=['Albuterol'],
    last_visit_id='V2303'
)
```

This is a useful Python technique when dictionary keys match function parameter names.

---

## 🚦 Validation Rules

The program follows these rules:

| **Field**       | **Validation Rule**                 |
| --------------- | ----------------------------------- |
| `patient_id`    | String matching `p` + digits        |
| `age`           | Integer greater than or equal to 18 |
| `gender`        | `male` or `female`                  |
| `diagnosis`     | String or `None`                    |
| `medications`   | List containing only strings        |
| `last_visit_id` | String matching `v` + digits        |

The complete record must also:

| **Structure**   | **Requirement**           |
| --------------- | ------------------------- |
| Input           | List or tuple             |
| Record          | Dictionary                |
| Dictionary keys | Exactly the required keys |

---

## 🧠 Boolean Logic

This project uses Boolean values extensively.

A Boolean can contain one of two values:

```python
True
```

or:

```python
False
```

For example:

```python
is_invalid = False
```

means that no invalid record has been found yet.

The validation expressions also produce Boolean results.

For example:

```python
age >= 18
```

produces either:

```text
True
```

or:

```text
False
```

### `and`

The `and` operator requires **both conditions** to be true.

```python
isinstance(age, int) and age >= 18
```

For example:

```text
age = 34
```

Both conditions are true, so the result is:

```text
True
```

### `or`

The `or` operator requires **at least one condition** to be true.

```python
isinstance(diagnosis, str) or diagnosis is None
```

Either the diagnosis can be a string or it can be `None`.

### `not`

The `not` operator reverses a Boolean value.

For example:

```python
is_invalid = False
```

then:

```python
not is_invalid
```

produces:

```text
True
```

The project uses `not` when checking for invalid conditions.

---

## 🔎 Regular Expressions

The project uses Python's `re` module to validate IDs.

```python
import re
```

Regular expressions allow the program to describe patterns that strings must follow.

### Patient ID Pattern

```python
p\d+
```

This requires:

```text
p
```

followed by one or more digits.

Examples:

```text
P1001
p1002
P12345
```

### Visit ID Pattern

```python
v\d+
```

This requires:

```text
v
```

followed by one or more digits.

Examples:

```text
V2301
v2302
V12345
```

### `re.fullmatch()`

The program uses:

```python
re.fullmatch()
```

because the **entire string** must match the required pattern.

This prevents extra characters from being accepted before or after the expected ID.

### `re.IGNORECASE`

The flag:

```python
re.IGNORECASE
```

makes the pattern case-insensitive.

Therefore:

```text
P1001
```

and:

```text
p1001
```

are both accepted.

---

## 📚 Concepts Practiced

This project reinforces the following Python concepts:

| **Concept**               | **Example**                                       |
| ------------------------- | ------------------------------------------------- |
| Variables                 | `is_invalid = False`                              |
| Lists                     | `medical_records = [...]`                         |
| Dictionaries              | `{'patient_id': 'P1001', ...}`                    |
| Sets                      | `key_set = set(...)`                              |
| Tuples                    | `isinstance(data, (list, tuple))`                 |
| Boolean values            | `True`, `False`                                   |
| Type checking             | `isinstance(age, int)`                            |
| Comparison operators      | `age >= 18`                                       |
| Logical `and`             | `isinstance(age, int) and age >= 18`              |
| Logical `or`              | `isinstance(diagnosis, str) or diagnosis is None` |
| Logical `not`             | `if not value`                                    |
| Functions                 | `validate()`                                      |
| Function parameters       | `find_invalid_records(...)`                       |
| Regular expressions       | `re.fullmatch('p\d+', ...)`                       |
| Case-insensitive matching | `re.IGNORECASE`                                   |
| List comprehensions       | `[key for key, value in ...]`                     |
| `all()`                   | `all([...])`                                      |
| `enumerate()`             | `for index, dictionary in enumerate(data)`        |
| Dictionary unpacking      | `find_invalid_records(**dictionary)`              |
| `continue`                | Skip an invalid record                            |
| `return`                  | Return validation results                         |
| Conditional statements    | `if` statements                                   |
| `print()` function        | Display validation messages                       |

---

## 📤 Expected Output

With the supplied `medical_records`:

```python
validate(medical_records)
```

all records satisfy the defined validation rules.

Therefore, the expected output is:

```text
Valid format.
```

The function returns:

```python
True
```

---

## ❌ Example of Invalid Data

For example, if a record contains an invalid age:

```python
{
    'patient_id': 'P1005',
    'age': 15,
    'gender': 'Female',
    'diagnosis': 'Asthma',
    'medications': ['Albuterol'],
    'last_visit_id': 'V2305',
}
```

the age validation:

```python
isinstance(age, int) and age >= 18
```

will evaluate to:

```text
False
```

The field can therefore be identified as invalid.

This demonstrates how the validator can detect problems with individual pieces of structured data.

---

## ▶️ How to Run

Make sure **Python 3** is installed on your computer.

Save the program in a Python file:

```text
medical_data_validator.py
```

Then run:

```bash
python medical_data_validator.py
```

On systems where Python 3 is accessed using `python3`, run:

```bash
python3 medical_data_validator.py
```

No external packages are required because `re` is part of Python's standard library.

---

## 🎯 Learning Goal

The main goal of this project is to build a strong foundation in **Python data validation and logical decision-making**.

The exercise demonstrates how Python can combine:

* Data structures
* Type checking
* Boolean logic
* Conditional statements
* Regular expressions
* Functions
* List comprehensions

to validate structured information.

These concepts provide a foundation for more advanced Python topics such as **file processing, APIs, databases, data cleaning, data analysis, automation, and machine learning**.

## 📖 Source

This project was completed as part of the **freeCodeCamp Python v9 Medical Data Validator workshop**.

## 👩‍💻 Author

**Asfia Aiman**

Part of my Python learning journey with **freeCodeCamp**.
