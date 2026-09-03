**# Travel Weather Planner**

A beginner-friendly Python project that practices **booleans, conditional statements, comparison operators, logical operators, and nested conditionals** by building a travel weather planner.

**## 📌 Problem**

Build a travel weather planner that determines whether a user can commute based on:

* Distance to travel in miles
* Whether it is raining
* Whether the user has a bicycle
* Whether the user has a car
* Whether the user has a ride-share app

The program should:

1. Check whether a valid distance has been provided.
2. Determine whether commuting is possible for distances of 1 mile or less.
3. Determine whether commuting is possible for distances between 1 and 6 miles.
4. Determine whether commuting is possible for distances greater than 6 miles.
5. Consider weather conditions when deciding whether walking or cycling is possible.
6. Check whether a bicycle, car, or ride-share option is available.
7. Print `True` or `False` based on the commuting conditions.

**## 🛠️ Technologies Used**

* **Python 3**
* Boolean values
* `if`, `elif`, and `else`
* Comparison operators
* Logical operators: `and`, `or`, `not`
* Nested conditional statements
* Variables
* `print()` function

**## 🚀 How It Works**

**### 1. Set the Travel Information**

The program starts by defining the distance, weather conditions, and available transportation options:

```python
distance_mi = 0
is_raining = True
has_bike = True
has_car = True
has_ride_share_app = True
```

These variables are used by the conditional statements to determine whether commuting is possible.

**### 2. Check for a Falsy Distance**

The program first checks whether `distance_mi` is a falsy value, such as `0`:

```python
if not distance_mi:
    print(False)
```

If there is no distance to travel, the program prints `False`.

**### 3. Check Distances of 1 Mile or Less**

For a distance of **1 mile or less**, commuting is possible only when it is not raining:

```python
elif distance_mi <= 1:
    if not is_raining:
        print(True)
    else:
        print(False)
```

The `not` operator checks whether it is **not raining**.

If it is raining, the program prints `False`.

**### 4. Check Distances Between 1 and 6 Miles**

For distances **greater than 1 mile and up to 6 miles**, the user must have a bicycle and it must not be raining:

```python
elif distance_mi <= 6:
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)
```

The `and` operator means both conditions must be true:

* The user must have a bike.
* It must not be raining.

If either condition is false, commuting is not possible.

**### 5. Check Distances Greater Than 6 Miles**

For distances **greater than 6 miles**, the user can commute if they have a car **or** a ride-share app:

```python
else:
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)
```

The `or` operator means that only one of the transportation options needs to be available.

**### 6. Commuting Conditions**

The program follows these rules:

| Distance            | Conditions                     | Result  |
| ------------------- | ------------------------------ | ------- |
| `0` or falsy        | No distance                    | `False` |
| `≤ 1 mile`          | Not raining                    | `True`  |
| `≤ 1 mile`          | Raining                        | `False` |
| `> 1 and ≤ 6 miles` | Bike available and not raining | `True`  |
| `> 1 and ≤ 6 miles` | No bike or raining             | `False` |
| `> 6 miles`         | Car or ride-share available    | `True`  |
| `> 6 miles`         | No car and no ride-share       | `False` |

**### 7. Display the Result**

The program uses the `print()` function to display whether commuting is possible:

```python
print(True)
```

or:

```python
print(False)
```

The result depends on the distance, weather, and available transportation.

**## 📤 Expected Output**

With the current values:

```python
distance_mi = 0
is_raining = True
has_bike = True
has_car = True
has_ride_share_app = True
```

The distance is a falsy value, so the expected output is:

```text
False
```

For example, if the values were:

```python
distance_mi = 3
is_raining = False
has_bike = True
has_car = False
has_ride_share_app = False
```

The expected output would be:

```text
True
```

**## 📚 Concepts Practiced**

| Concept              | Example                               |
| -------------------- | ------------------------------------- |
| Variables            | `distance_mi = 0`                     |
| Booleans             | `is_raining = True`                   |
| Comparison operators | `distance_mi <= 1`                    |
| `if` statement       | `if not distance_mi:`                 |
| `elif` statement     | `elif distance_mi <= 6:`              |
| `else` statement     | `else:`                               |
| `and` operator       | `has_bike and not is_raining`         |
| `or` operator        | `has_car or has_ride_share_app`       |
| `not` operator       | `not is_raining`                      |
| Nested conditionals  | Conditions inside another conditional |
| `print()` function   | `print(True)`                         |

**## ▶️ How to Run**

Make sure Python 3 is installed.

From the project directory, run:

```bash
python index.py
```

**## 🎯 Learning Goal**

The goal of this project is to understand how Python makes decisions using **conditional statements and Boolean logic**, while applying those concepts to a practical travel and weather scenario.

**## 👩‍💻 Author**

**Asfia Aiman**

Part of my Python learning journey with **freeCodeCamp**.
