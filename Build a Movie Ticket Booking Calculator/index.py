# Problem:
# Build a movie ticket booking calculator using booleans and
# conditional statements. The program checks the user's age,
# membership status, weekend/show time, seat type, and calculates
# discounts, extra charges, service charges, and the final ticket price.


base_price = 15

age = 21

seat_type = 'Gold'

show_time = 'Evening'


# Check if the user is old enough to book a ticket
if age > 17:
    print('User is eligible to book a ticket')


# Check if the user is eligible for Evening shows
if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')


# Check membership discount eligibility
is_member = False

is_weekend = False

discount = 0

if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')

print('Discount:', discount)


# Calculate extra charges
extra_charges = 0

if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')

print('Extra charges:', extra_charges)


# Check the main ticket booking condition
if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')

    # Calculate service charges based on seat type
    service_charges = 0

    if seat_type == 'Premium':
        service_charges = 5

    elif seat_type == 'Gold':
        service_charges = 3

    else:
        service_charges = 1

    print('Service charges:', service_charges)


    # Calculate final ticket price
    final_price = base_price + extra_charges + service_charges - discount

    print('Final price of ticket:', final_price)

else:
    print('Ticket booking failed due to restrictions')