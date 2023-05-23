"""The main function on this document is write and append text to enthropy2"""

def main_write():
    """We need to perform a main function and respond in order of UI/UX)
    Note that setting the mode to w overwrites all the existing data in the file.
    Go to oneappend to write without loosing the text inside the file"""
    filename = "nonexistent_file.txt"
    try:
        ent_write()
        as_list()
        main_append()
    except OSError as e:
        raise OSError(f"Error opening file '{filename}': {e.strerror}") from e

def ent_write():
    """Trying tho write some text"""
    ent = 'enthropy2.txt'
    with open(ent, 'w+') as writefile1:
        writefile1.write("This is an space to create enthropy without thermodynamics \n")
        writefile1.write("But be careful everything is thermodynamics \n")
        writefile1.write("Thermodynamics is like  \n")
        writefile1.truncate()
    with open(ent, 'r+') as testwritefile1:
        print(testwritefile1.read())
    print(writefile1.closed)

def as_list():
    """Just declaring a list"""
    lines = ["you can create something but can dissapear at all \n", "Matter just change into other forms. \n"]
    with open("enthropy2.txt", 'w+') as writefile2:
        for line in lines:
            writefile2.write(line)
            writefile2.truncate()
    with open("enthropy2.txt", 'r', encoding="UTF-8") as testreadfile2:
        print(testreadfile2.read())
    print(writefile2.closed)

def main_append():
    """This calls the functions to append text, is needed to declare a main function
    to not change all the code just few parts"""
    append_one()

def append_one():
    """What we append will be here"""
    with open ("enthropy2.txt", 'a+') as testappend1:
        # testappend1.seek(0, 2)
        testappend1.write("Thermodynamics laws define the fundamental physical quantities like energy, \n")
        testappend1.write("temperature and entropy that characterize thermodynamic systems at thermal equilibrium.\n")
        testappend1.write("These thermodynamics laws represent how these quantities behave under various circumstances.\n")
    with open("enthropy2.txt", 'r') as testappend2:
        print (testappend2.read())
    print (testappend1.closed)
    print (testappend1.closed)

main_write()
