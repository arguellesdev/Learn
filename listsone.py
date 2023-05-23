"""This is a document for Create a list but also work with tupples which are inmuttable"""

def name_artist():
    """define a list """
    # \n By default, the print() function adds a newline character
    #  at the end of each line it prints
    L = ["Michael Jackson", 10.1, 1982]
    print('the same element using negative and positive indexing:\n Postive:',L[0],
    '\n Negative:' , L[-3]  )
    print('the same element using negative and positive indexing:\n Postive:',L[1],
    '\n Negative:' , L[-2]  )
    print('the same element using negative and positive indexing:\n Postive:',L[2],
    '\n Negative:' , L[-1]  )

name_artist()
