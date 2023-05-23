"""defining new on old python version f use form"""

def python_old():
    """Checking how to code old versions"""
    name_1= str(input("What is your name? "))
    age_1= int(input("What is your age? "))
    message = "My name is %s and I am %d years old" % (name_1, age_1)
    message=message.title()
    # this is how we did it before, maybe your course have this code, update your knowledge please
    print(message)
# %s is used as a placeholder for a string value. When the %s placeholder is used in a string,
# it means that a string value will be inserted in its place.
# %d is used as a placeholder for an integer value.
def python_new():
    """new versions of python"""
    name_2 = str(input("What is your name? "))
    age_2=  int(input("What is your age? "))
    message = f"My name is {name_2} and I am {age_2} years old".title()
    print(message)
python_old()
python_new()
