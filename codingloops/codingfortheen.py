"""Today reviewed Python documentation on https://docs.python.org/3/library/intro.html
to improve my knowledge """


def loops():
    """for it is a word that does exist in other languages but
    does not necessarily have as many features as other languages"""

    while True:
        meow_num = input("Enter the times you want(1-10): ")
        if meow_num.isdigit() and int(meow_num) <= 10:
            break
#ve como agrear str sin que haga loop en break
    for _ in range(int(meow_num)):
        print ("meow")

loops()
