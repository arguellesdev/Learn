"""Today reviewed Python documentation on https://docs.python.org/3/library/intro.html
to improve my knowledge """


def loops():
    """for it is a word that does exist in other languages but
    does not necessarily have as many features as other languages"""
    meow_num = input("Enter the times you want: ")
    if meow_num.isnumeric():
        for i in range(int(meow_num)):
            print("meow")
            i -=1
        if int(meow_num) > 9:
            error()
    else:
        error()

def error():
    """not succes cases"""
    print ("Let's try again, enter a valid number. ")
    loops ()

loops()
