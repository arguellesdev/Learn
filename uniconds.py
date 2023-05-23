"""the use of conditions is to track where the datas entropy begins"""

    # equal: ==
    # not equal: !=
    # greater than: >
    # less than: <
    # greater than or equal to: >=
    # less than or equal to: <=
def tecatesonoro():
    """defining welcome to everyone"""
    print("Welcome to Tecate Sonoro")
    agelimit()


def agelimit():
    """what is your age"""
    age = int(input('What is your age? ' ))
    #expression that can be true or false
    if age == 18:
        print('you can enter to 5 concerts only' )
        year_song=int(input("What's the release year of watermelon sugar? "))
        if year_song == 2019:
            print ("next question")
            g_input = input("if you want more need to answer this question, What was John Legend's first hit song? ")
            if g_input == "used to love you":
                print ('you can access all the concerts')
            else:
                print ("almost")
        else:
            print ("still 5 concerts")
    elif age >= 19:
        print ('you can access all the concerts')
    else:
        print ('you are not allowed to be in this event' )
    #The statements after the if statement will run regardless if the condition is true or false
    print("See ya")

tecatesonoro()
