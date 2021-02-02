def fullName(first, last):
    if not isinstance(first, str) or not isinstance(last, str) or not first.isalnum() or not last.isalnum():
        print("That's not a valid name")
        return None
    if not first or not last:
        print("Please include both first and last name")
        return None
    return first + " " + last

