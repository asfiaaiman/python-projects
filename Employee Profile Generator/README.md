# Employee Badge & Code Analyzer

A beginner-friendly Python project built to practice the fundamentals of **string manipulation**, **string concatenation**, **f-strings**, **type conversion**, and **string slicing**.

The project generates formatted employee information and extracts useful information from an employee code.

## 📌 Project Overview

This project demonstrates how Python strings can be combined, formatted, and sliced to create useful employee-related information.

It creates:

* An employee's full name
* Employee address
* Employee age information
* Years of experience
* A formatted employee badge
* Department code
* Year code
* Employee initials
* Last three digits of an employee code

## 🛠️ Technologies Used

* **Python 3**
* String concatenation
* f-strings
* String slicing
* Type conversion using `str()`

## 🚀 How It Works

### 1. Create the Employee Name

The first and last names are combined using the `+` operator:

```python
first_name = 'John'
last_name = 'Doe'

full_name = first_name + ' ' + last_name
```

Result:

```text
John Doe
```

### 2. Build the Address

The address is extended using the `+=` operator:

```python
address = '123 Main Street'
address += ', Apartment 4B'
```

Result:

```text
123 Main Street, Apartment 4B
```

### 3. Create Employee Information

The employee's age is converted from an integer to a string using `str()` and combined with other strings:

```python
employee_age = 28

employee_info = full_name + ' is ' + str(employee_age) + ' years old'
```

Output:

```text
John Doe is 28 years old
```

### 4. Display Experience

The employee's years of experience are also converted to a string:

```python
experience_years = 5

experience_info = 'Experience: ' + str(experience_years) + ' years'
```

Output:

```text
Experience: 5 years
```

### 5. Generate an Employee Badge

An f-string is used to create a formatted employee badge:

```python
position = 'Data Analyst'
salary = 75000

employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
```

Output:

```text
Employee: John Doe | Age: 28 | Position: Data Analyst | Salary: $75000
```

## 🔎 Employee Code Analysis

The employee code is:

```python
employee_code = 'DEV-2026-JD-001'
```

The code contains several pieces of information separated by hyphens.

### Department

The first three characters are extracted using string slicing:

```python
department = employee_code[0:3]
```

Output:

```text
DEV
```

### Year

Characters from index `4` through `7` are extracted:

```python
year_code = employee_code[4:8]
```

Output:

```text
2026
```

### Employee Initials

The initials are extracted using:

```python
initials = employee_code[9:11]
```

Output:

```text
JD
```

### Last Three Characters

Negative indexing is used to retrieve the final three characters:

```python
last_three = employee_code[-3:]
```

Output:

```text
001
```

## 📚 Concepts Practiced

This project reinforces the following Python concepts:

| Concept              | Example                        |
| -------------------- | ------------------------------ |
| Variables            | `employee_age = 28`            |
| String concatenation | `first_name + ' ' + last_name` |
| String conversion    | `str(employee_age)`            |
| `+=` operator        | `address += ', Apartment 4B'`  |
| f-strings            | `f'Employee: {full_name}'`     |
| String slicing       | `employee_code[0:3]`           |
| Negative indexing    | `employee_code[-3:]`           |
| Printing output      | `print(employee_info)`         |

## ▶️ How to Run

Make sure Python 3 is installed on your computer.

Save the code in a Python file, for example:

```text
employee_badge.py
```

Then run:

```bash
python employee_badge.py
```

## 📤 Expected Output

```text
John Doe is 28 years old
Experience: 5 years
Employee: John Doe | Age: 28 | Position: Data Analyst | Salary: $75000
DEV
2026
JD
001
```

## 🎯 Learning Goal

The main goal of this project is to build a strong foundation in Python string manipulation before moving on to more advanced concepts such as functions, lists, dictionaries, loops, and data processing.

## 👩‍💻 Author

**Asfia Aiman**

Built as part of my Python learning journey with **freeCodeCamp**.
