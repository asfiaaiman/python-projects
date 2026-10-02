Build a Planet Class

A beginner-friendly Python project built to practice the fundamentals of Object-Oriented Programming (OOP), including classes, objects, constructors, instance attributes, methods, self, type checking, exception handling, f-strings, return statements, and special methods.

The project creates Planet objects, validates their data, provides information about their orbit, and defines how each planet is displayed when printed.

📌 Project Overview

This project demonstrates how Python classes can be used to create and manage objects with their own data and behavior.

A Planet class is created as a blueprint for individual planets.

Each planet stores:

The planet name
The planet type
The star it orbits

The class also provides two methods:

orbit() - returns information about the planet's orbit
__str__() - returns a formatted description of the planet

Three planet objects are created:

planet_1 = Planet('Mercury', 'terrestrial', 'Sun')
planet_2 = Planet('Venus', 'terrestrial', 'Sun')
planet_3 = Planet('Earth', 'terrestrial', 'Sun')

The program then prints each planet and its orbit information.

🛠️ Technologies Used
Python 3
Classes
Objects
__init__() constructor
Instance attributes
self
Methods
__str__() special method
isinstance()
Exception handling
TypeError
ValueError
f-strings
print()
return
Dot notation
🚀 How It Works
1. Create the Planet Class

The project starts by defining a class named Planet:

class Planet:

A class acts as a blueprint for creating objects.

In this project, the blueprint defines the information and behavior that every planet object should have.

2. Create the __init__() Method

The class contains an __init__() method:

def __init__(self, name, planet_type, star):

The __init__() method runs automatically whenever a new Planet object is created.

It has four parameters:

self - refers to the current object
name - the name of the planet
planet_type - the classification of the planet
star - the star the planet orbits
3. Validate the Data Types

Before storing the values, the program checks that all three arguments are strings:

if not isinstance(name, str) or not isinstance(planet_type, str) or not isinstance(star, str):
    raise TypeError('name, planet type, and star must be strings')

The isinstance() function checks whether a value belongs to a particular data type.

For example:

isinstance('Earth', str)

returns:

True

But:

isinstance(123, str)

returns:

False

If any value is not a string, the program raises a TypeError.

4. Validate Empty Strings

The program also checks that none of the values are empty:

if not name or not planet_type or not star:
    raise ValueError('name, planet_type, and star must be non-empty strings')

An empty string evaluates to False in Python.

Therefore:

not ''

evaluates to:

True

If any required value is empty, the program raises a ValueError.

5. Store Instance Attributes

After validation, the values are stored as instance attributes:

self.name = name
self.planet_type = planet_type
self.star = star

Each object gets its own values.

For example:

planet_1 = Planet('Mercury', 'terrestrial', 'Sun')

stores:

name → Mercury
planet_type → terrestrial
star → Sun

Another object:

planet_3 = Planet('Earth', 'terrestrial', 'Sun')

stores:

name → Earth
planet_type → terrestrial
star → Sun

The same class can therefore create many objects with different data.

6. Create the orbit() Method

The class contains an orbit() method:

def orbit(self):
    return f'{self.name} is orbiting around {self.star}...'

This method uses the object's name and star attributes.

For example:

print(planet_1.orbit())

produces:

Mercury is orbiting around Sun...

The method uses return instead of print() so that the generated string can be used elsewhere in the program.

7. Create the __str__() Method

The class also defines a special method named __str__():

def __str__(self):
    return f'Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}'

The __str__() method controls how an object is represented when passed to print().

For example:

print(planet_1)

automatically calls:

planet_1.__str__()

and produces:

Planet: Mercury | Type: terrestrial | Star: Sun
8. Create the Planet Objects

Three planet objects are created from the Planet class:

planet_1 = Planet('Mercury', 'terrestrial', 'Sun')
planet_2 = Planet('Venus', 'terrestrial', 'Sun')
planet_3 = Planet('Earth', 'terrestrial', 'Sun')

Each object has its own values.

Attribute	planet_1	planet_2	planet_3
name	Mercury	Venus	Earth
planet_type	terrestrial	terrestrial	terrestrial
star	Sun	Sun	Sun
9. Call the orbit() Method

The program calls the orbit() method for each planet:

print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())

The output is:

Mercury is orbiting around Sun...
Venus is orbiting around Sun...
Earth is orbiting around Sun...
10. Print the Planet Objects

The program then prints each planet directly:

print(planet_1)
print(planet_2)
print(planet_3)

Because the class has a __str__() method, Python automatically uses it when displaying the objects.

The output is:

Planet: Mercury | Type: terrestrial | Star: Sun
Planet: Venus | Type: terrestrial | Star: Sun
Planet: Earth | Type: terrestrial | Star: Sun
🪐 Planet Class Logic

The basic structure of the project is:

Planet Class
     ↓
Create Planet Object
     ↓
Validate Data Types
     ↓
Validate Non-Empty Values
     ↓
Store Instance Attributes
     ↓
Call orbit()
     ↓
Return Orbit Information
     ↓
Print Planet Object
     ↓
__str__() Formats Planet Information
📝 Example Planet

One of the planet objects is:

planet_3 = Planet('Earth', 'terrestrial', 'Sun')

Its attributes are:

name → Earth
planet_type → terrestrial
star → Sun

Calling:

print(planet_3.orbit())

produces:

Earth is orbiting around Sun...

Calling:

print(planet_3)

produces:

Planet: Earth | Type: terrestrial | Star: Sun
📤 Expected Output

Running the complete program produces:

Mercury is orbiting around Sun...
Venus is orbiting around Sun...
Earth is orbiting around Sun...
Planet: Mercury | Type: terrestrial | Star: Sun
Planet: Venus | Type: terrestrial | Star: Sun
Planet: Earth | Type: terrestrial | Star: Sun
📚 Concepts Practiced

This project reinforces the following Python concepts:

Concept	Example
Classes	class Planet:
Objects	planet_1, planet_2, planet_3
Constructor	__init__()
Parameters	name, planet_type, star
Instance attributes	self.name, self.planet_type, self.star
self	self.name
Methods	orbit()
Special methods	__str__()
Type checking	isinstance(name, str)
Exceptions	raise TypeError
Exceptions	raise ValueError
f-strings	f'{self.name}...'
return	return f'...'
print()	print(planet_1)
Dot notation	planet_1.name
Method calls	planet_1.orbit()
▶️ How to Run

Make sure Python 3 is installed on your computer.

Save the program in a Python file:

index.py

Then run:

python index.py

On systems where Python 3 is accessed using python3, run:

python3 index.py
🎯 Learning Goal

The main goal of this project is to build a strong foundation in Object-Oriented Programming (OOP) with Python.

The exercise demonstrates how to:

Create classes
Create objects from classes
Initialize objects using __init__()
Store data using instance attributes
Use self
Validate input using isinstance()
Raise TypeError and ValueError
Create and call methods
Return values from methods
Define special methods such as __str__()
Access attributes using dot notation
Format strings using f-strings

These concepts provide a foundation for more advanced Python topics such as inheritance, encapsulation, polymorphism, abstraction, data models, APIs, and larger object-oriented applications.

👩‍💻 Author

Asfia Aiman

Part of my Python learning journey with freeCodeCamp.