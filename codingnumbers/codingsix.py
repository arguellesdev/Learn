"""Entendiendo otros condicionales. Modulus operator % returns a remainder of dividing two numbers.
he term modulo comes from a branch of mathematics called modular arithmetic. 
Modular arithmetic deals with integer arithmetic on a circular number line that
has a fixed set of numbers. All arithmetic operations performed on this number 
line will wrap around when they reach a certain number called the modulus."""

def modulus():
    """la vie est belle"""
    x_value = int(input("enter a number "))
    if x_value % 2 == 0:
        print ("even")
    elif x_value % 3 == 0:
        print("May the force be with you")
    else:
        print("odd")
        return modulus ()
modulus()
