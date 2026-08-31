# Movie Ticket Booking Calculator

A beginner-friendly Python project that practices **booleans, conditional statements, comparison operators, logical operators, nested conditionals, and arithmetic operations** by building a movie ticket booking calculator.

## 📌 Problem

Build a movie ticket booking calculator that determines whether a user can book a movie ticket and calculates the final ticket price based on:

* User's age
* Seat type
* Show time
* Membership status
* Whether it is a weekend

The program should:

1. Check whether the user is eligible to book a ticket.
2. Check whether the user is eligible for an Evening show.
3. Determine whether the user qualifies for a membership discount.
4. Apply extra charges for weekend or Evening shows.
5. Calculate service charges based on the selected seat type.
6. Check the final ticket booking conditions.
7. Calculate and display the final ticket price.

## 🛠️ Technologies Used

* **Python 3**
* Boolean values
* `if`, `elif`, and `else`
* Comparison operators
* Logical operators: `and`, `or`
* Nested conditional statements
* Arithmetic operations
* Variables

## 🚀 How It Works

### 1. Set the Ticket Information

The program starts by defining the base ticket price and customer information:

```python
base_price = 15
age = 21
seat_type = 'Gold'
show_time = 'Evening'
```

### 2. Check Ticket Eligibility

The program checks whether the user is older than 17:

```python
if age > 17:
    print('User is eligible to book a ticket')
```

It also checks whether the user is at least 21 years old for Evening shows:

```python
if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')
```

### 3. Calculate Membership Discount

The program checks two conditions using the `and` operator:

```python
if is_member and age >= 21:
    discount = 3
```

The user must be a member **and** at least 21 years old to receive the discount.

### 4. Calculate Extra Charges

The program applies an additional charge when it is a weekend **or** the show is in the Evening:

```python
if is_weekend or show_time == 'Evening':
    extra_charges = 2
```

### 5. Check Booking Conditions

The main booking condition uses both `or` and `and`:

```python
if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')
```

This determines whether the user's ticket booking can proceed.

### 6. Calculate Service Charges

Service charges depend on the seat type:

```python
if seat_type == 'Premium':
    service_charges = 5
elif seat_type == 'Gold':
    service_charges = 3
else:
    service_charges = 1
```

The available service charges are:

| Seat Type | Service Charge |
| --------- | -------------: |
| Premium   |             $5 |
| Gold      |             $3 |
| Other     |             $1 |

### 7. Calculate the Final Price

The final ticket price is calculated using:

```python
final_price = base_price + extra_charges + service_charges - discount
```

With the current values:

```text
Base price:       $15
Extra charges:     $2
Service charges:   $3
Discount:          $0
----------------------
Final price:      $20
```

## 📤 Expected Output

```text
User is eligible to book a ticket
User is eligible for Evening shows
User does not qualify for membership discount
Discount: 0
Extra charges will be applied
Extra charges: 2
Ticket booking condition satisfied
Service charges: 3
Final price of ticket: 20
```

## 📚 Concepts Practiced

| Concept              | Example                                                   |
| -------------------- | --------------------------------------------------------- |
| Variables            | `age = 21`                                                |
| Booleans             | `is_member = False`                                       |
| Comparison operators | `age >= 21`                                               |
| `if` statement       | `if age > 17:`                                            |
| `elif` statement     | `elif seat_type == 'Gold':`                               |
| `else` statement     | `else:`                                                   |
| `and` operator       | `is_member and age >= 21`                                 |
| `or` operator        | `is_weekend or show_time == 'Evening'`                    |
| Nested conditionals  | Conditional statements inside another condition           |
| Arithmetic           | `base_price + extra_charges + service_charges - discount` |

## ▶️ How to Run

Make sure Python 3 is installed.

From the project directory, run:

```bash
python index.py
```

## 🎯 Learning Goal

The goal of this project is to understand how Python makes decisions using **conditional statements and Boolean logic**, while applying those concepts to a practical problem.

## 👩‍💻 Author

**Asfia Aiman**

Part of my Python learning journey with **freeCodeCamp**.
