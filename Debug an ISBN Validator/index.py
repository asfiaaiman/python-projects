def calculate_check_digit_10(digits):
    total = sum((10 - i) * digit for i, digit in enumerate(digits))
    remainder = total % 11
    check_digit = (11 - remainder) % 11

    if check_digit == 10:
        return 'X'

    return str(check_digit)


def calculate_check_digit_13(digits):
    total = 0

    for i, digit in enumerate(digits):
        if i % 2 == 0:
            total += digit
        else:
            total += digit * 3

    check_digit = (10 - (total % 10)) % 10

    return str(check_digit)


def validate_isbn(isbn, length):
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return

    main_digits = isbn[0:length - 1]
    given_check_digit = isbn[length - 1]

    try:
        main_digits_list = [int(digit) for digit in main_digits]
    except ValueError:
        print('Invalid character was found.')
        return

    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)

    if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')


def main():
    user_input = input('Enter ISBN and length: ')

    if ',' not in user_input:
        print('Enter comma-separated values.')
        return

    values = user_input.split(',')

    isbn = values[0]
    length = values[1]

    if not length.isdigit():
        print('Length must be a number.')
        return

    length = int(length)

    if length == 10 or length == 13:
        validate_isbn(isbn, length)
    else:
        print('Length should be 10 or 13.')


# main()