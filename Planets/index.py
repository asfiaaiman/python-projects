# Define the Planet class.
# This class acts as a blueprint for creating planet objects.
class Planet:

    # Initialize a new Planet object.
    # self refers to the current object.
    # name, planet_type, and star are provided when creating the object.
    def __init__(self, name, planet_type, star):

        # Check that all three values are strings.
        # Raise a TypeError if any value is not a string.
        if not isinstance(name, str) or not isinstance(planet_type, str) or not isinstance(star, str):
            raise TypeError('name, planet type, and star must be strings')

        # Check that none of the values are empty strings.
        # Raise a ValueError if any value is empty.
        if not name or not planet_type or not star:
            raise ValueError('name, planet_type, and star must be non-empty strings')

        # Store the planet name as an instance attribute.
        self.name = name

        # Store the planet type as an instance attribute.
        self.planet_type = planet_type

        # Store the star as an instance attribute.
        self.star = star

    # Define a method that returns information about the planet's orbit.
    def orbit(self):

        # Return a formatted string containing the planet and its star.
        return f'{self.name} is orbiting around {self.star}...'

    # Define the __str__ method.
    # This controls how the Planet object is displayed when printed.
    def __str__(self):

        # Return a formatted description of the planet.
        return f'Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}'


# Create the first Planet object.
planet_1 = Planet('Mercury', 'terrestrial', 'Sun')

# Create the second Planet object.
planet_2 = Planet('Venus', 'terrestrial', 'Sun')

# Create the third Planet object.
planet_3 = Planet('Earth', 'terrestrial', 'Sun')


# Call the orbit method for each planet and print the returned string.
print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())


# Print each planet object.
# Python automatically calls the __str__ method.
print(planet_1)
print(planet_2)
print(planet_3)