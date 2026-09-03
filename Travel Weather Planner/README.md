# Travel Weather Planner

A beginner-friendly Python project built to practice the fundamentals of **Boolean values**, **conditional statements**, **comparison operators**, **logical operators**, and **nested conditionals**.

The project determines whether a user can commute based on the travel distance, weather conditions, and available transportation options.

## 📌 Project Overview

This project demonstrates how Python can use Boolean logic and conditional statements to make decisions based on different travel conditions.

It checks:

* Distance to travel in miles
* Whether it is raining
* Whether the user has a bicycle
* Whether the user has a car
* Whether the user has a ride-share app
* Whether commuting is possible under the given conditions

## 🛠️ Technologies Used

* **Python 3**
* Boolean values
* `if`, `elif`, and `else`
* Comparison operators
* Logical operators: `and`, `or`, `not`
* Nested conditional statements
* Variables
* `print()` function

## 🚀 How It Works

### 1. Set the Travel Information

The program starts by defining the distance, weather conditions, and available transportation options:

```python
distance_mi = 0
is_raining = True
has_bike = True
has_car = True
has_ride_share_app = True
```

These variables are used by the conditional statements to determine whether commuting is possible.

The Boolean variables contain either `True` or `False` and represent whether a particular condition is active or available.

### 2. Check for a Falsy Distance

The program first checks whether the travel distance is a falsy value:

```python
if not distance_mi:
    print(False)
```

In Python, `0` is considered a **falsy value**.

Since the current value is:

```python
distance_mi = 0
```

the condition:

```python
not distance_mi
```

evaluates to `True`.

Therefore, the program prints:

```text
False
```

### 3. Check Distances of 1 Mile or Less

For a distance of **1 mile or less**, commuting is possible only when it is not raining:

```python
elif distance_mi <= 1:
    if not is_raining:
        print(True)
    else:
        print(False)
```

The comparison operator:

```python
distance_mi <= 1
```

checks whether the distance is less than or equal to 1 mile.

The `not` operator is then used to check whether it is **not raining**.

If:

```python
is_raining = False
```

the user can commute.

If:

```python
is_raining = True
```

the program prints:

```text
False
```

### 4. Check Distances Between 1 and 6 Miles

For distances **greater than 1 mile and up to 6 miles**, the user must have a bicycle and it must not be raining:

```python
elif distance_mi <= 6:
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)
```

The `and` operator means that **both conditions must be true**.

The user must:

* Have a bicycle
* Not be traveling in the rain

For example:

```python
distance_mi = 3
is_raining = False
has_bike = True
```

Both conditions are satisfied, so the result is:

```text
True
```

If there is no bicycle or it is raining, the result is:

```text
False
```

### 5. Check Distances Greater Than 6 Miles

For distances **greater than 6 miles**, the program checks whether the user has a car or a ride-share app:

```python
else:
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)
```

The `or` operator means that **at least one condition must be true**.

The user can commute if they have:

* A car, or
* A ride-share app

For example:

```python
has_car = True
has_ride_share_app = False
```

The user still has a transportation option, so the result is:

```text
True
```

If both are unavailable:

```python
has_car = False
has_ride_share_app = False
```

the result is:

```text
False
```

## 🚦 Commuting Conditions

The program follows these rules:

| **Distance**        | **Conditions**                 | **Result** |
| ------------------- | ------------------------------ | ---------- |
| `0` or falsy        | No distance                    | `False`    |
| `≤ 1 mile`          | Not raining                    | `True`     |
| `≤ 1 mile`          | Raining                        | `False`    |
| `> 1 and ≤ 6 miles` | Bike available and not raining | `True`     |
| `> 1 and ≤ 6 miles` | No bike or raining             | `False`    |
| `> 6 miles`         | Car or ride-share available    | `True`     |
| `> 6 miles`         | No car and no ride-share       | `False`    |

This creates a simple decision-making system based on distance, weather, and transportation.

## 🧠 Boolean Logic

This project uses three important logical operators.

### `not`

The `not` operator reverses a Boolean value.

For example:

```python
is_raining = False

not is_raining
```

produces:

```text
True
```

It is used in the program to determine whether it is safe to walk or cycle based on the weather.

### `and`

The `and` operator requires **both conditions** to be true.

```python
has_bike and not is_raining
```

For example:

```text
has_bike = True
is_raining = False
```

Both conditions are satisfied, so the result is:

```text
True
```

### `or`

The `or` operator requires **at least one condition** to be true.

```python
has_car or has_ride_share_app
```

For example:

```text
has_car = True
has_ride_share_app = False
```

The first condition is true, so the result is:

```text
True
```

Python, mercifully, makes this part rather readable.

## 🔎 Nested Conditionals

The project also demonstrates **nested conditional statements**.

A conditional statement is placed inside another conditional:

```python
elif distance_mi <= 1:
    if not is_raining:
        print(True)
    else:
        print(False)
```

The outer condition determines the travel distance.

The inner condition then determines whether the weather allows the user to commute.

Nested conditionals are useful when one decision depends on another decision.

## 📤 Expected Output

With the initial values:

```python
distance_mi = 0
is_raining = True
has_bike = True
has_car = True
has_ride_share_app = True
```

the distance is `0`, which is a falsy value.

Therefore, the expected output is:

```text
False
```

Another example:

```python
distance_mi = 3
is_raining = False
has_bike = True
has_car = False
has_ride_share_app = False
```

The distance is between 1 and 6 miles, the user has a bicycle, and it is not raining.

The expected output is:

```text
True
```

## 📚 Concepts Practiced

This project reinforces the following Python concepts:

| **Concept**          | **Example**                     |
| -------------------- | ------------------------------- |
| Variables            | `distance_mi = 0`               |
| Boolean values       | `is_raining = True`             |
| Comparison operators | `distance_mi <= 1`              |
| `if` statement       | `if not distance_mi:`           |
| `elif` statement     | `elif distance_mi <= 6:`        |
| `else` statement     | `else:`                         |
| `and` operator       | `has_bike and not is_raining`   |
| `or` operator        | `has_car or has_ride_share_app` |
| `not` operator       | `not is_raining`                |
| Nested conditionals  | `if` inside another `if`        |
| Falsy values         | `distance_mi = 0`               |
| `print()` function   | `print(True)`                   |

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

## 🎯 Learning Goal

The main goal of this project is to build a strong foundation in Python **Boolean logic and conditional decision-making**.

The exercise demonstrates how multiple conditions can be combined using `and`, `or`, and `not` to create practical decision-making logic.

These concepts provide a foundation for more advanced Python topics such as **loops, functions, lists, dictionaries, error handling, and data processing**.

## 👩‍💻 Author

**Asfia Aiman**

Part of my Python learning journey with **freeCodeCamp**.
