"""This module is to learn coding with floats and basic algebra"""
# define happy path
# define sad __path__
# define edge cases
def sotol():
    """This function calculates exponential of two input values"""
    x_value = input("What is x? ")
    if x_value.isnumeric():
        x_value = float(x_value) # print(f"{round(x_value):.1f}")
        print(f"{round(x_value):,.2f}")
    else:
    # if not x_value.isnumeric(): #check if x_value is a number
        print ("insert a valid number".capitalize())
        sotol()
    y_value = input("What is y? ")
    if y_value.isnumeric():
        y_value = float(y_value)
        print(f"{round(y_value):,.2f}")
    else:
    # if not y_value.isnumeric():
        #check if y_value is a number
        print ("insert a valid number".capitalize())
        sotol()
    result = x_value ** y_value
    result = float(result)
    if x_value > y_value:
        print(f"{result:,.2f}, Welcome nerdy!".title())
        quit()
    elif x_value == y_value:
        print("increase x value".capitalize())
        sotol()
    else:
        print("you are in a Schodinger box, star again dude")
        sotol()
sotol()
