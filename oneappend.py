"""This is created to append text without loosing the contents on a file"""
# remember to create a file such as enthropy2.txt before with touch!
def main_append():
    """This calls the functions to append text, is needed to declare a main function
    to not change all the code just few parts"""
    filename = "nonexistent_file.txt"
    try:
        append_one()
    except OSError as e:
        raise OSError(f"Error opening file '{filename}': {e.strerror}") from e
def append_one():
    """What we append will be here"""
    with open ("enthropy2.txt", 'a+') as testappend1: #put enthropy2 or 3 or 4 to try
        # testappend1.seek(0, 2)
        testappend1.write("The zeroth law of thermodynamics states that if there are two bodies (A and B)\n")
        testappend1.write("that are in thermal equilibrium with another body (third body as C) \n")
        testappend1.write("then these two bodies are also in thermal equilibrium with each another. \n")
        testappend1.write("Since such a conclusion may seem trivial and easy to reach,\n")
        testappend1.write("some may feel that it is not worth being one of the basic laws of thermodynamics.  \n")
        testappend1.write("Source: Ibrahim Dincer, in Comprehensive Energy Systems, 2018.\n")

    with open("enthropy2.txt", 'r') as testappend2:
        print (testappend2.read())
    print (testappend1.closed)
    print (testappend1.closed)

def merge():
    with open('entrophy2.txt','r') as readfile:
        with open('enthropy2.txt','a+') as writefile: # change mode to 'a'
            for line in readfile:
                    writefile.write(line)
            # The loop variable line is not a function, but rather a variable that is used
            # to store the current line of text that is being read from the file.
            # In each iteration of the loop, line is set to the next line of text from the
            # file until the end of the file is reached.
            # The loop is commonly used when working with files to read and process the contents
            # of the file line by line. This can be useful for many purposes, such as searching
            # for a specific pattern in the file, extracting specific data from the file,
            # or modifying the contents of the file.
# It's fairly ineffecient to open the file in a or w and then reopening it in r to read any lines.
# Luckily we can access the file in the following modes:

#     r+ : Reading and writing. Cannot truncate the file.
#     w+ : Writing and reading. Truncates the file.
#     a+ : Appending and Reading. Creates a new file, if none exists. For example instead put enthropy2.txt we will gonna put enthropy3.txt
main_append()
