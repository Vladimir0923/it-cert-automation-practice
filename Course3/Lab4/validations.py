#!/usr/bin/env python3

import re

import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")

    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        return False

    # Define a new regular expression pattern
    pattern = '^[a-z][a-z0-9._]*$'

    # Check if the first character is a letter
    if not re.match('^[a-z]', username):
        return False

    # Use the new pattern for validation
    if re.match(pattern, username):
        return True

    return False

print(validate_user("blue.kale", 3))     # True
print(validate_user(".blue.kale", 3))    # False
print(validate_user("red_quinoa", 4))    # True
print(validate_user("_red_quinoa", 4))   # False
