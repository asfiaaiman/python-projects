# Define the MusicalInstrument class
class MusicalInstrument:

    # Initialize a new musical instrument with a name and instrument type
    def __init__(self, name, instrument_type):
        self.name = name
        self.instrument_type = instrument_type

    # Define a method that prints a message about playing the instrument
    def play(self):
        print(f'The {self.name} is fun to play!')

    # Define a method that returns a fact about the instrument
    def get_fact(self):
        return f'The {self.name} is part of the {self.instrument_type} family of instruments.'


# Create the first MusicalInstrument instance
instrument_1 = MusicalInstrument('Oboe', 'woodwind')

# Create the second MusicalInstrument instance
instrument_2 = MusicalInstrument('Trumpet', 'brass')


# Play the first instrument
instrument_1.play()

# Print a fact about the first instrument
print(instrument_1.get_fact())


# Play the second instrument
instrument_2.play()

# Print a fact about the second instrument
print(instrument_2.get_fact())