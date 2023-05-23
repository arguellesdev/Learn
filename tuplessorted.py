"""trying to sort a tuple"""
def sorting():
    """show the entropy of home"""
    tupleb = input('born years of all family members of your house: '.capitalize()).split()
    print(tupleb)
    tuplebsorted = sorted(tupleb)
    print(tuplebsorted)

def sorting2list():
    """first convert to a list then go back to tupple"""
    tuplea = ('ACDC', 'War machine', 2008)
    list_of_tuples = [(year, album, artist) for (artist, album, year) in [tuplea]]
    # Swap the elements of the tuple and convert to a list of tuples
    sorted_list = sorted(list_of_tuples)
    # Sort the list based on the year
    sorted_tuple = tuple([(album, artist, year) for (year, album, artist) in sorted_list])
    # Convert the sorted list back into a tuple
    print(sorted_tuple)
    # Output: ('War machine', 'ACDC', 1986)

sorting()
