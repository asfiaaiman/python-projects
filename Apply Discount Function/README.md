# Apply Discount Function

A beginner-friendly Python project that practices **functions, parameters, data type validation, conditional statements, arithmetic operators, and return values** by building a function that calculates the final price of an item after applying a percentage discount.

## 📌 Problem

Build an `apply_discount` function that calculates the final price of an item after applying a percentage discount.

The function should:

1. Accept the item's price and discount percentage as parameters.
2. Check whether the price is a valid number.
3. Check whether the discount is a valid number.
4. Check whether the price is greater than `0`.
5. Check whether the discount is between `0` and `100`.
6. Calculate the discount amount when both inputs are valid.
7. Return the final price after applying the discount.
8. Return an appropriate error message when an input is invalid.

For example, if the price is `50` and the discount is `20%`, the discount amount is `10`, so the final price is `40`.

## 🛠️ Technologies Used

* **Python 3**
* Functions
* Function parameters
* `isinstance()`
* `int` and `float` data types
* `if` statements
* Comparison operators
* Arithmetic operators
* `return` statements
* Variables

## 🚀 How It Works

### 1. Define the Function

The program starts by defining a function named `apply_discount` with exactly two parameters:

```python
def apply_discount(price, discount):
```

The `price` parameter represents the original price of the item, while `discount` represents the discount percentage.

### 2. Validate the Price

The function first checks whether `price` is a number:

```python
if not isinstance(price, (int, float)):
    return "The price should be a number."
```

The `isinstance()` function checks whether the value belongs to the `int` or `float` data type.

If the price is not a number, the function returns:

```text
The price should be a number.
```

### 3. Validate the Discount

The function then checks whether `discount` is a number:

```python
if not isinstance(discount, (int, float)):
    return "The discount should be a number."
```

If the discount is not an integer or floating-point number, the function returns:

```text
The discount should be a number.
```

### 4. Check Whether the Price Is Greater Than 0

The price must be greater than `0`:

```python
if price <= 0:
    return "The price should be greater than 0."
```

If the price is `0` or a negative number, the function returns an error message instead of calculating a discount.

### 5. Validate the Discount Range

The discount must be between `0` and `100`:

```python
if discount < 0 or discount > 100:
    return "The discount should be between 0 and 100."
```

The `or` operator checks whether the discount is either below `0` or above `100`.

For example:

* `-10` is invalid.
* `0` is valid.
* `50` is valid.
* `100` is valid.
* `120` is invalid.

### 6. Calculate the Discount Amount

When both inputs are valid, the function calculates the discount amount:

```python
discount_amount = price * discount / 100
```

For example, with a price of `50` and a discount of `20%`:

```text
50 × 20 ÷ 100 = 10
```

The discount amount is therefore `10`.

### 7. Calculate the Final Price

The discount amount is subtracted from the original price:

```python
return price - discount_amount
```

For example:

```text
50 - 10 = 40
```

The final price is `40`.

### 8. Discount Conditions

The function follows these rules:

| Input                    | Condition            | Result                                        |
| ------------------------ | -------------------- | --------------------------------------------- |
| `price`                  | Not a number         | `"The price should be a number."`             |
| `discount`               | Not a number         | `"The discount should be a number."`          |
| `price`                  | `≤ 0`                | `"The price should be greater than 0."`       |
| `discount`               | `< 0` or `> 100`     | `"The discount should be between 0 and 100."` |
| Valid price and discount | `discount = 0`       | Original price                                |
| Valid price and discount | `discount = 100`     | `0`                                           |
| Valid price and discount | `0 < discount < 100` | Discounted price                              |

## 📤 Expected Output

For example:

```python
apply_discount(100, 20)
```

The calculation is:

```text
100 × 20 ÷ 100 = 20
100 - 20 = 80
```

The expected result is:

```text
80
```

Another example:

```python
apply_discount(200, 50)
```

The expected result is:

```text
100
```

A discount of `0%` returns the original price:

```python
apply_discount(50, 0)
```

Expected result:

```text
50
```

A discount of `100%` reduces the final price to zero:

```python
apply_discount(100, 100)
```

Expected result:

```text
0
```

The function also supports floating-point values:

```python
apply_discount(74.5, 20.0)
```

Expected result:

```text
59.6
```

## 📚 Concepts Practiced

| Concept                | Example                                |
| ---------------------- | -------------------------------------- |
| Functions              | `def apply_discount(price, discount):` |
| Parameters             | `price`, `discount`                    |
| Data type checking     | `isinstance(price, (int, float))`      |
| Integers               | `100`, `50`                            |
| Floating-point numbers | `74.5`, `20.0`                         |
| `if` statement         | `if price <= 0:`                       |
| Comparison operators   | `discount > 100`                       |
| Logical operators      | `discount < 0 or discount > 100`       |
| Arithmetic operators   | `price * discount / 100`               |
| Variables              | `discount_amount`                      |
| `return` statement     | `return price - discount_amount`       |
| Error handling         | Returning validation messages          |

## ▶️ How to Run

Make sure Python 3 is installed.

From the project directory, run:

```bash
python index.py
```

The function can also be tested directly in Python:

```python
print(apply_discount(100, 20))
```

Expected output:

```text
80
```

## 🎯 Learning Goal

The goal of this project is to understand how to create and use **Python functions with parameters**, validate input values using `isinstance()`, make decisions using **conditional statements**, perform calculations using **arithmetic operators**, and return appropriate results.

This project is part of practicing fundamental Python programming concepts through a practical price and discount calculation.

## 👩‍💻 Author

**Asfia Aiman**

Part of my Python learning journey with **freeCodeCamp**.
