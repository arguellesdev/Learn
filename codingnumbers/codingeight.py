"""BOOLEAN TRUE FALSE"""

def modulus3():
    """la vie est belle"""
    x_value = input("enter a number ")
    # x_value = int(x_value)
    if character(x_value):
        print("enter a valid number")
        return modulus3()
    elif is_even(x_value):
        print ("even")
    else:
        print("odd")
        return x_value

def is_even(n_value):
    """simplifing condition"""
    return True if n_value % 2 ==0 else False

def character(n_value):
    """not characters on equation"""
    return False if n_value is int else True

modulus3()
