def averageElements(arr):
    if not arr:
        print("List is empty")
        return None
    if not isinstance(arr, list):
        print("That's not a list!")
        return None
    return sum(arr) / len(arr)