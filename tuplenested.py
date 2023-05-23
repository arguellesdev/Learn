"""Welcome to entrophy tupple file"""

def nt_entrophy():
    """put everything"""
    nt = ((input('your fav singer: '), input('your fav song: ')), 1986, 'may the forth be with you', 5,
          (input("describe the song with one word: "), 'kindness'))
    print(len(nt))
    main_theme(nt)
    initial(nt)

def in_description(nt):
    "entire description of user input"""
    print("Element 0 of Tuple: ", nt[0])
    print("Element 1 of Tuple: ", nt[1])
    print("Element 2 of Tuple: ", nt[2])
    print("Element 3 of Tuple: ", nt[3])
    print("Element 4 of Tuple: ", nt[4])


def main_theme(nt):
    """just the important data"""
    print("Artist: ", nt[0] [0])
    print('Song: ', nt[0] [1])
    print("What is the topic: ", nt[4] [0])

def initial(nt):
    """just the important data"""
    print("Artist: ", nt[0] [0] [0])
    print('Song: ', nt[0] [1] [0])
    print("What is the topic: ", nt[4] [0] [0])

    nt_entrophy()
