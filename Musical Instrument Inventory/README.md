# Musical Instrument Inventory

A beginner-friendly Python project built to practice the fundamentals of **classes**, **objects**, **constructors**, **instance attributes**, **methods**, **`self`**, **f-strings**, **return statements**, and **dot notation**.

The project creates musical instrument objects and allows each instrument to display a message about playing it and return a fact about its instrument family.

## 📌 Project Overview

This project demonstrates the basics of **Object-Oriented Programming (OOP)** in Python.

A `MusicalInstrument` class is created as a blueprint for individual musical instruments.

Each instrument object stores:

* The instrument name
* The instrument type

The class also provides two methods:

* `play()` - prints a message about playing the instrument
* `get_fact()` - returns a fact about the instrument

Two instrument objects are created:

```python
instrument_1 = MusicalInstrument('Oboe', 'woodwind')
instrument_2 = MusicalInstrument('Trumpet', 'brass')
```

The program then calls the methods on both objects.

## 🛠️ Technologies Used

* **Python 3**
* Classes
* Objects
* `__init__()` constructor
* Instance attributes
* `self`
* Methods
* f-strings
* `print()`
* `return`
* Dot notation

## 🚀 How It Works

### 1. Create the MusicalInstrument Class

The project starts by defining a class named `MusicalInstrument`:

```python
class MusicalInstrument:
```

A class acts as a **blueprint** for creating objects.

In this project, the blueprint describes what information and behavior a musical instrument should have.

### 2. Create the `__init__()` Method

The class contains an `__init__()` method:

```python
def __init__(self, name, instrument_type):
```

The `__init__()` method runs automatically whenever a new `MusicalInstrument` object is created.

It accepts two parameters:

* `name` - the name of the instrument
* `instrument_type` - the instrument's family or type

### 3. Store Instance Attributes

The parameters are assigned to instance attributes:

```python
self.name = name
self.instrument_type = instrument_type
```

`self` refers to the specific object being created.

For example:

```python
instrument_1 = MusicalInstrument('Oboe', 'woodwind')
```

creates an object with:

```text
name → Oboe
instrument_type → woodwind
```

Another object:

```python
instrument_2 = MusicalInstrument('Trumpet', 'brass')
```

has:

```text
name → Trumpet
instrument_type → brass
```

Each object stores its own values.

### 4. Create the `play()` Method

The class contains a method named `play()`:

```python
def play(self):
    print(f'The {self.name} is fun to play!')
```

The method only requires `self` because it accesses the instrument's existing `name` attribute.

For example:

```python
instrument_1.play()
```

produces:

```text
The Oboe is fun to play!
```

And:

```python
instrument_2.play()
```

produces:

```text
The Trumpet is fun to play!
```

### 5. Create the `get_fact()` Method

The class also contains a method named `get_fact()`:

```python
def get_fact(self):
    return f'The {self.name} is part of the {self.instrument_type} family of instruments.'
```

This method uses the instrument's:

* `name`
* `instrument_type`

It creates a sentence using an f-string.

For example:

```python
instrument_1.get_fact()
```

returns:

```text
The Oboe is part of the woodwind family of instruments.
```

### 6. Use `return` Instead of `print`

The `get_fact()` method uses `return`:

```python
return f'The {self.name} is part of the {self.instrument_type} family of instruments.'
```

This is different from the `play()` method, which uses `print()`:

```python
print(f'The {self.name} is fun to play!')
```

`print()` displays a value directly.

`return` sends a value back to the code that called the method.

Therefore, this:

```python
print(instrument_1.get_fact())
```

first gets the string from `get_fact()` and then prints it.

### 7. Create the Instrument Objects

Two objects are created from the `MusicalInstrument` class:

```python
instrument_1 = MusicalInstrument('Oboe', 'woodwind')
instrument_2 = MusicalInstrument('Trumpet', 'brass')
```

The first object represents an Oboe.

The second object represents a Trumpet.

Although both objects come from the same class, they contain different data.

### 8. Access Attributes Using Dot Notation

The attributes of an object can be accessed using dot notation:

```python
instrument_1.name
instrument_1.instrument_type
```

For example:

```python
print(instrument_1.name)
```

produces:

```text
Oboe
```

Similarly:

```python
print(instrument_2.instrument_type)
```

produces:

```text
brass
```

The general syntax is:

```python
object_name.attribute_name
```

### 9. Call Methods Using Dot Notation

Methods can also be called using dot notation:

```python
instrument_1.play()
instrument_1.get_fact()
```

The object name comes first, followed by the method name.

The parentheses `()` execute the method.

## 🎵 Musical Instrument Logic

The basic structure of the project is:

```text
MusicalInstrument Class
        ↓
Create Object
        ↓
Store Name + Instrument Type
        ↓
Call play()
        ↓
Display Playing Message
        ↓
Call get_fact()
        ↓
Return Instrument Family Fact
```

Each object has its own data while sharing the same methods defined by the class.

## 📝 Example Objects

The project creates two musical instruments:

```python
instrument_1 = MusicalInstrument('Oboe', 'woodwind')
instrument_2 = MusicalInstrument('Trumpet', 'brass')
```

Their stored information can be represented as:

| **Attribute**     | **instrument_1** | **instrument_2** |
| ----------------- | ---------------- | ---------------- |
| `name`            | `Oboe`           | `Trumpet`        |
| `instrument_type` | `woodwind`       | `brass`          |

Both objects use the same class but contain different attribute values.

## 📤 Expected Output

The following code:

```python
instrument_1.play()

print(instrument_1.get_fact())

instrument_2.play()

print(instrument_2.get_fact())
```

produces:

```text
The Oboe is fun to play!
The Oboe is part of the woodwind family of instruments.
The Trumpet is fun to play!
The Trumpet is part of the brass family of instruments.
```

## 📚 Concepts Practiced

This project reinforces the following Python concepts:

| **Concept**         | **Example**                         |
| ------------------- | ----------------------------------- |
| Classes             | `class MusicalInstrument:`          |
| Objects             | `instrument_1`, `instrument_2`      |
| Constructor         | `__init__()`                        |
| Parameters          | `name`, `instrument_type`           |
| Instance attributes | `self.name`, `self.instrument_type` |
| `self`              | `self.name`                         |
| Methods             | `play()`, `get_fact()`              |
| f-strings           | `f'The {self.name}...'`             |
| `print()`           | `print(...)`                        |
| `return`            | `return f'...'`                     |
| Dot notation        | `instrument_1.name`                 |
| Method calls        | `instrument_1.play()`               |

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

The main goal of this project is to build a strong foundation in **Object-Oriented Programming (OOP)** with Python.

The exercise demonstrates how to:

* Create a class
* Create objects from a class
* Initialize objects using `__init__()`
* Store information using instance attributes
* Use `self`
* Create and call methods
* Access attributes using dot notation
* Return values from methods
* Format strings using f-strings

These concepts provide a foundation for more advanced Python and software development topics such as **inheritance, encapsulation, polymorphism, abstract classes, data models, APIs, and larger object-oriented applications**.

## 👩‍💻 Author

**Asfia Aiman**

Part of my Python learning journey with **freeCodeCamp**.
