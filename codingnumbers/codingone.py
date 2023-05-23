"""This module is to learn coding with floats and basic algebra"""
def sotol():
    """This function calculates exponential of two input values"""
    x_value = input("What is x? ")
    if x_value.isnumeric():
        x_value = float(x_value) # print(f"{round(x_value):.1f}")
        print(f"{round(x_value):,f}")
    else:
    # if not x_value.isnumeric(): #check if x_value is a number
        print ("insert a valid number".capitalize())
        sotol()
    y_value = input("What is y? ")
    if y_value.isnumeric():
        y_value = float(y_value)
        print(f"{round(y_value):,f}")
    else:
    # if not y_value.isnumeric():
        #check if y_value is a number
        print ("insert a valid number".capitalize())
        sotol()
    try:
        result = x_value ** y_value
        # "try" is a special keyword in Python that allows us to execute a block of code
        # and catch any exceptions that might occur while the code is executing.
        # When an exception is raised inside a "try" block,
        # Python looks for an "except" block that matches the type of the exception
        # that was raised. If it finds a match, it executes the code inside that "except"
        # block to handle the exception.
    except OverflowError:
        print("The result is out of range for a numerical calculation.")
        sotol()
    if x_value > y_value:
        print(float(result), "welcome nerdy".title())
        quit()
    elif x_value == y_value:
        print("increase x value".capitalize())
        sotol()
    else:
        print("you are in a Schodinger box, star again dude")
        sotol()

sotol()
