# Distance the user needs to travel, in miles
distance_mi = 0

# True if it is currently raining
is_raining = True

# True if the user has a bicycle
has_bike = True

# True if the user has a car
has_car = True

# True if the user has a ride-share app
has_ride_share_app = True


# If the distance is 0 or another falsy value, commuting is not possible
if not distance_mi:
    print(False)

# If the distance is 1 mile or less,
# the user can commute only if it is not raining
elif distance_mi <= 1:
    if not is_raining:
        print(True)
    else:
        print(False)

# If the distance is more than 1 mile and up to 6 miles,
# the user needs a bike and the weather must not be rainy
elif distance_mi <= 6:
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)

# If the distance is more than 6 miles,
# the user can commute if they have a car OR a ride-share app
else:
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)