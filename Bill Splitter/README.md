# Bill Splitter

A beginner-friendly Python project that calculates a restaurant bill, adds a tip, divides the final amount among friends, and rounds the amount each person needs to pay.

This project was created to practice **numbers, mathematical operations, variables, arithmetic operators, and rounding in Python**.

## 📌 Problem

Build a bill splitter that calculates the total cost of appetizers, main courses, desserts, and drinks.

The program should:

1. Calculate the total bill.
2. Add a 25% tip.
3. Calculate the total bill including the tip.
4. Divide the final bill equally among 4 friends.
5. Round the amount each person pays to 2 decimal places.

## 🛠️ Technologies Used

* **Python 3**
* Variables
* Arithmetic operators
* `+=` operator
* Division
* Multiplication
* `round()` function

## 🚀 How It Works

### 1. Initialize the Running Total

The program starts with a total of zero:

```python
running_total = 0
```

The number of friends is set to 4:

```python
num_of_friends = 4
```

### 2. Store the Food and Drink Costs

The prices are stored in separate variables:

```python
appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21
```

### 3. Calculate the Total Bill

All expenses are added to the running total:

```python
running_total += appetizers + main_courses + desserts + drinks
```

The bill before the tip is:

```text
198.83
```

### 4. Calculate the Tip

The program calculates a 25% tip:

```python
tip = running_total * 0.25
```

The tip is approximately:

```text
49.71
```

### 5. Add the Tip

The tip is added to the original bill:

```python
running_total += tip
```

The total including the tip is approximately:

```text
248.54
```

### 6. Split the Bill

The final bill is divided equally among 4 friends:

```python
final_bill = running_total / num_of_friends
```

Each person's share is approximately:

```text
62.13
```

### 7. Round the Final Amount

The amount is rounded to two decimal places:

```python
each_pays = round(final_bill, 2)
```

## 📤 Expected Output

```text
Total bill so far: 198.82999999999998
Tip amount: 49.707499999999995
Total with tip: 248.53749999999998
Bill per person: 62.13437499999999
Each person pays: 62.13
```

The long decimal values are a result of Python's floating-point representation. The final amount is rounded to **2 decimal places** for a practical bill amount.

## 📚 Concepts Practiced

| Concept                | Example                          |
| ---------------------- | -------------------------------- |
| Variables              | `num_of_friends = 4`             |
| Floating-point numbers | `appetizers = 37.89`             |
| Addition               | `appetizers + main_courses`      |
| Multiplication         | `running_total * 0.25`           |
| Division               | `running_total / num_of_friends` |
| `+=` operator          | `running_total += tip`           |
| Rounding               | `round(final_bill, 2)`           |
| Output                 | `print()`                        |

## ▶️ How to Run

Make sure Python 3 is installed.

Run the following command from the project directory:

```bash
python index.py
```

## 🎯 Learning Goal

The goal of this project is to strengthen the fundamentals of working with numbers and mathematical operations in Python by solving a simple real-world problem: **splitting a restaurant bill among friends**.

## 👩‍💻 Author

**Asfia Aiman**

Part of my Python learning journey with **freeCodeCamp**.
