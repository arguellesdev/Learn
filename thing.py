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