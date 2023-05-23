"""Entendiendo otros condicionales. Modulus operator % returns a remainder of dividing two numbers.
he term modulo comes from a branch of mathematics called modular arithmetic. 
Modular arithmetic deals with integer arithmetic on a circular number line that
has a fixed set of numbers. All arithmetic operations performed on this number 
line will wrap around when they reach a certain number called the modulus."""

def modulus2():
    """la vie est belle"""
    x_value = int(input("enter a number "))
    if is_even(x_value):
        print ("even")
    else:
        print("odd")
        return modulus2()
def is_even(n_value):
    """defining condition"""
    if n_value % 2 ==0:
        return True
    elif n_value % 3 == 0:
        print("May the force be with you")
    else:
        return False

modulus2()
