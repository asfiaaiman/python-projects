# RPG Character Builder
# This program creates a character with three stats:
# Strength, Intelligence, and Charisma.


# Characters used to display the stats.
full_dot = '●'
empty_dot = '○'


def create_character(name, strength, intelligence, charisma):
    """
    Create an RPG character after validating the name and stats.

    Parameters:
        name (str): The character's name.
        strength (int): Strength stat from 1 to 4.
        intelligence (int): Intelligence stat from 1 to 4.
        charisma (int): Charisma stat from 1 to 4.

    Returns:
        str: An error message if validation fails,
             otherwise the character and its stats.
    """

    # -------------------------
    # Validate character name
    # -------------------------

    # The character name must be a string.
    if not isinstance(name, str):
        return 'The character name should be a string'

    # The character name cannot be empty.
    if name == '':
        return 'The character should have a name'

    # The character name cannot be longer than 10 characters.
    if len(name) > 10:
        return 'The character name is too long'

    # The character name cannot contain spaces.
    if ' ' in name:
        return 'The character name should not contain spaces'

    # -------------------------
    # Validate character stats
    # -------------------------

    # All three stats must be integers.
    if (
        not isinstance(strength, int)
        or not isinstance(intelligence, int)
        or not isinstance(charisma, int)
    ):
        return 'All stats should be integers'

    # Every stat must be at least 1.
    if strength < 1 or intelligence < 1 or charisma < 1:
        return 'All stats should be no less than 1'

    # Every stat must be at most 4.
    if strength > 4 or intelligence > 4 or charisma > 4:
        return 'All stats should be no more than 4'

    # The three stats must use exactly 7 points in total.
    if strength + intelligence + charisma != 7:
        return 'The character should start with 7 points'

    # -------------------------
    # Create the character
    # -------------------------

    # Create the visual bar for each stat.
    # Full dots represent the points the character has.
    # Empty dots fill the remaining spaces up to 10.
    strength_bar = full_dot * strength + empty_dot * (10 - strength)
    intelligence_bar = full_dot * intelligence + empty_dot * (10 - intelligence)
    charisma_bar = full_dot * charisma + empty_dot * (10 - charisma)

    # Return the character information as four lines.
    return (
        name
        + '\nSTR ' + strength_bar
        + '\nINT ' + intelligence_bar
        + '\nCHA ' + charisma_bar
    )


# Example usage.
print(create_character('ren', 4, 2, 1))