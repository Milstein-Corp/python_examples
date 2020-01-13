import json


# all values from old dictionary will be replace by the new dictonary values.
def merge_dicts(old, new):
    return {**old, **new}

old_info = {
    "firstname": "Kevin",
    "phone_number": "+33 1 23 45 67 89"
}

new_info = {
    "phone_number": "+33 6 88 88 88 88",
    "email": "sabbe.kev@gmail.com"
}

print(json.dumps(merge_dicts(old_info, new_info), indent=4))
# {
#     "firstname": "Kevin",
#     "phone_number": "+33 6 88 88 88 88",
#     "email": "sabbe.kev@gmail.com"
# }
