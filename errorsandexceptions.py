"""This file is to lear how to get a file if gryffindor
try:
    # some code that might raise an exception
except ExceptionClass:
    # handle the exception
    In this syntax, ExceptionClass is the name of the exception class
    you want to catch. For example, if you want to catch a TypeError,
    you would use except TypeError:
"""
def with_():
    """checking differences between the use of with. Using a "with" statement to open a file is
        better practice because it automatically closes the file"""
    filename = "nonexistent_file.txt"
    try:
        writetext()
        readtext()
        read_parts()
    except OSError as e:
        raise OSError(f"Error opening file '{filename}': {e.strerror}") from e
def writetext():
    """write different text on files needs to declare in one line but encoding is important"""
    with open("enthropy.txt","w", encoding="UTF-8") as file1:
        #  to write "r" (read mode), "w" (write mode) or "a" (append mode).
        file_stuff=file1.write("I'm back, I'm ready to get my Ph.D done!")
        print("The change of text give us", file_stuff, " characters")
    print(file1.closed)
def readtext():
    """read the entire text as a test that was changed"""
    with open("enthropy.txt","r", encoding="UTF-8") as file2:
        file_content=file2.read()
        print(file_content)
    print(file2.closed)
def file_characteristics():
    """This function is declare to know the characteristics """
    with open("enthropy.txt","w", encoding="UTF-8") as filec:
            print(filec.mode)
            print(filec.name)
            print (type(filec))
def read_parts():
    """Read certain amount of characters"""
    with open("enthropy.txt","r", encoding="UTF-8") as file3:
        #if you put a number on parenthesis only will read the number of characters you declare to read.
        print(file3.read(4))
        print(file3.read(4))
        print(file3.read(7))
        print(file3.read(15))
    print(file3.closed)
# Here's how it works:
#The string is enclosed in double quotes, which indicates that it is a string literal.
#The f at the beginning of the string indicates that it is an f-string.
# F-strings are a feature introduced in Python 3.6 that allow you to embed expressions
# inside string literals, using curly braces {} to indicate where the expressions should be inserted.
#Inside the string, there are two expressions that are enclosed in curly braces. The first expression is filename,
# which is a variable that holds the name of the file that was being opened.
# The second expression is e.strerror, which is a property of the OSError object that holds a string describing
# the error that occurred.
#The expressions are enclosed in curly braces {}, and are preceded by a dollar sign $ in older versions of Python(< 3.6),
# but are not required in Python 3.6 or later.
#The expressions are evaluated at runtime, and their values are inserted into the string in place of the curly braces.
def condit():
    """large coding, refactorize needed"""
    try:
        getfile = open("enthropy.txt", "w", encoding="utf-8")
        #  to write "r" (read mode), "w" (write mode) or "a" (append mode).
        getfile.write("I'm back, I'm ready to get my Ph.D done!")
    except OSError:
        # The IOError and OSError exceptions both represent errors
        # related to input/output (I/O) operations,
        print ("Unable to open or read the data in file.")
        #IOError was the exception class used in Python 2 to represent I/O errors,
        # but it has been deprecated in Python 3 and replaced with OSError.
        # However, IOError is still available in Python 3 for backwards compatibility reasons.
    else:
        print("The file was written successfully")
        # The else block executes if there was no exception raised
        # in the try block. It simply prints a success message.
    finally:
        getfile.close()
        print("File is now close")
        #he finally block executes regardless of whether there was
        # an exception or not. It closes the file (if it was opened)
with_()
