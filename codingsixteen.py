def loops():
    """for it is a word that does exist in other languages but
    does not necessarily have as many features as other languages"""

    while True:
        meow_num = input("Enter the times you want(1-10): ")
        if int(meow_num) <= 10:
            break
#ve como agrear str sin que haga loop en break
    for _ in range(int(meow_num)):
        print ("meow")

loops()