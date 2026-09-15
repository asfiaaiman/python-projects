# Number Pattern Generator
# This program generates a sequence of numbers from 1 up to n.


def number_pattern(n):
    """
    Return a space-separated number pattern from 1 to n.

    Parameters:
        n: A positive integer that determines the end of the pattern.

    Returns:
        A string containing numbers from 1 to n,
        or an error message if n is invalid.
    """

    # Check whether n is an integer.
    if not isinstance(n, int):
        return 'Argument must be an integer value.'

    # Check whether n is greater than 0.
    if n <= 0:
        return 'Argument must be an integer greater than 0.'

    # Start with an empty string to build the number pattern.
    numbers = ''

    # Loop from 1 through n.
    # n + 1 is used because the ending value of range() is excluded.
    for i in range(1, n + 1):
        # Convert the current number to a string and add it to the pattern.
        numbers += str(i)

        # Add a space after each number except the last one.
        # This prevents an unnecessary trailing space.
        if i < n:
            numbers += ' '

    return numbers


# Example usage.
print(number_pattern(4))
print(number_pattern(12))