"""Indexing It is helpful to think of a string as an ordered sequence.
Each element in the sequence can be accessed using an index represented
by the array of numbers:
"""
def name_input():
    """We are looking for medication azitromicina"""
    Name= input('What is the medication are you looking for? ')
    print ('The number of characters in your that medication is ', len (Name), 'caracteres')
    # Slicing
    # print ("ok, I'm looking for ',  Name[0:5])"
    # print ('ok, I am looking for ',  Name[0:5])
    print ('ok, I\'m looking for ',  Name[0:5])
    try:
        if charactern_strings(Name):
            use_backlash(Name)
            negative_indexing_analysis(Name)
        else:
            raise ValueError("Try another name with an 'a' at the beggining")
    except ValueError as e:
        print(e)

def charactern_strings(Name):
    """looking for an at the beginning"""
    print(Name[0])
    print (Name[0:5:1])
    return 'azitr' in Name.lower()

def stride_analysis(Name):
    """looking for ina other parts of the word"""
    print (Name[::1])
    print (Name[::2])
    print (Name[::3])
    print (Name[0:5:2])

def negative_indexing_analysis(Name):
    """checking other characters"""
    print (Name[-2])
    return "n" in Name.lower()

def use_backlash(Name):
    """your name is right"""
    statin = Name + '\nis found in the system\n'
    print (2 * statin.capitalize())

name_input()
