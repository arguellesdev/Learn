"""This is a document for Create a list but also work with tupples which are inmuttable"""

def name_artist2():
    """define a list """
    # \n By default, the print() function adds a newline character
    #  at the end of each line it prints
    L = ["Michael Jackson", 10.1,1982,"MJ",1]
    print ('full or empty depends on your way to see life: \n Positive:', L[0], '\n Negative:' , L[-5])
    print (L[3:5])
    # SIf you want to print the slice without the square brackets, you can convert it to a string
    # and remove the brackets using string manipulation. One way to do this is to
    # use the join() method to concatenate the elements of the slice into a single string,
    # separated by a space or another character of your choice.
    # L = ["Michael Jackson", 10.1,1982,"MJ",1]
    # slice_str = ' '.join(str(elem) for elem in L[3:5])
    # print(slice_str)
    extend_proof(L)
    append_proof(L)
    changes(L)
    split_(L)

def extend_proof(L):
    """to define the use of extend"""
    music_gender = input('what is the type of music: '.capitalize())
    L.extend([music_gender, 10])
    print(L)

def append_proof(L):
    """to append"""
    song = input('what is your fav song: '. capitalize())
    L.append([song, 'one of my fav'])
    print (L)

def changes(L):
    """to make a few changes"""
    print ('before', L, len(L))
    L[0] = input ("What's your fav singer? ")
    del L[1:7]
    print ('after', L, len(L))

def split_(L):
    """to split actually"""
    A = L[0].split()
    del L[1:7]
    print(A)

name_artist2()
