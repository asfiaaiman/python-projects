import re

# A list containing medical records.
# Each record is stored as a dictionary with information about one patient.
medical_records = [
    {
        'patient_id': 'P1001',
        'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301',
    },
    {
        'patient_id': 'p1002',
        'age': 47,
        'gender': 'male',
        'diagnosis': 'Type 2 Diabetes',
        'medications': ['Metformin', 'Insulin'],
        'last_visit_id': 'v2302',
    },
    {
        'patient_id': 'P1003',
        'age': 29,
        'gender': 'female',
        'diagnosis': 'Asthma',
        'medications': ['Albuterol'],
        'last_visit_id': 'v2303',
    },
    {
        'patient_id': 'p1004',
        'age': 56,
        'gender': 'Male',
        'diagnosis': 'Chronic Back Pain',
        'medications': ['Ibuprofen', 'Physical Therapy'],
        'last_visit_id': 'V2304',
    }
]


def find_invalid_records(
    patient_id, age, gender, diagnosis, medications, last_visit_id
):
    # Store the validation result for each field in a dictionary.
    #
    # Each value will be True if the field is valid
    # and False if the field is invalid.
    constraints = {

        # patient_id must:
        # 1. Be a string
        # 2. Follow the pattern "p" followed by one or more digits.
        #
        # re.IGNORECASE allows both "p1001" and "P1001".
        'patient_id': isinstance(patient_id, str)
        and re.fullmatch('p\d+', patient_id, re.IGNORECASE),

        # age must be an integer and must be at least 18.
        'age': isinstance(age, int) and age >= 18,

        # gender must be a string and must be either "male" or "female".
        #
        # .lower() makes the comparison case-insensitive.
        # Therefore "Male", "MALE", and "male" are all accepted.
        'gender': isinstance(gender, str)
        and gender.lower() in ('male', 'female'),

        # diagnosis must either be a string or None.
        # None is allowed because a diagnosis may not have been provided.
        'diagnosis': isinstance(diagnosis, str) or diagnosis is None,

        # medications must be a list.
        # all() checks that every item inside the list is a string.
        'medications': isinstance(medications, list)
        and all([isinstance(i, str) for i in medications]),

        # last_visit_id must:
        # 1. Be a string
        # 2. Follow the pattern "v" followed by one or more digits.
        #
        # re.IGNORECASE allows both "v2301" and "V2301".
        'last_visit_id': isinstance(last_visit_id, str)
        and re.fullmatch('v\d+', last_visit_id, re.IGNORECASE)
    }

    # Loop through every field and return the names of fields
    # whose validation result is False.
    #
    # Example:
    # {'age': False, 'gender': True}
    # would return ['age'].
    return [key for key, value in constraints.items() if not value]


def validate(data):
    # Check whether the supplied data is a list or tuple.
    # The validator accepts either type.
    is_sequence = isinstance(data, (list, tuple))

    # If data is not a list or tuple, the entire input has an invalid format.
    if not is_sequence:
        print('Invalid format: expected a list or tuple.')
        return False

    # This keeps track of whether we found any invalid records.
    # It starts as False because we haven't found an error yet.
    is_invalid = False

    # These are the exact keys that every medical-record dictionary
    # is expected to contain.
    key_set = set(
        ['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id']
    )

    # enumerate() gives us both:
    # - index: the position of the record
    # - dictionary: the actual medical record
    for index, dictionary in enumerate(data):

        # Every item in the outer list/tuple must be a dictionary.
        if not isinstance(dictionary, dict):
            print(f'Invalid format: expected a dictionary at position {index}.')
            is_invalid = True

            # Skip this item and continue checking the remaining records.
            continue

        # Compare the dictionary's keys with the required set of keys.
        #
        # If they are different, the dictionary has a missing key,
        # an extra key, or an incorrect key.
        if set(dictionary.keys()) != key_set:
            print(
                f'Invalid format: {dictionary} at position {index} has missing and/or invalid keys.'
            )
            is_invalid = True

            # Don't try to validate the field values because
            # the structure of this record is already invalid.
            continue

        # Pass all dictionary values to find_invalid_records().
        #
        # **dictionary automatically matches each dictionary key
        # to the corresponding function parameter.
        invalid_records = find_invalid_records(**dictionary)

        # If one or more fields are invalid, mark the entire input as invalid.
        if invalid_records:
            print(
                f'Invalid field(s) at position {index}: {invalid_records}'
            )
            is_invalid = True

    # After checking every record, return False if any problem was found.
    if is_invalid:
        return False

    # If we reached here, every record passed validation.
    print('Valid format.')
    return True


# Run the validator using the medical_records list.
validate(medical_records)
