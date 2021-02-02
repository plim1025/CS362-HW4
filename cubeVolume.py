def cubeVolume(x):
    if(not isinstance(x, int)):
        print("That's not an integer")
        return -1
    if(x < 0):
        print("Length of cube cannot be negative")
        return -1
    return x**3
