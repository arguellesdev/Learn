"""BEFORE COMPLICATE"""
def hogwarts():
    """defining name"""
    input_name = str(input("What is your name? "))
    print(input_name)
    return gryffindor(input_name)

def gryffindor(input_name):
    """defining house"""
    # if input_name.lower() == "harry"
    if input_name.lower() in ["harry",  "hermione", "ron", "anya"]:
        print("Welcome to Gryffindor,".title(), input_name.title())
        return True
    else:
        hat()

def hat():
    """defining house if not gryffindor"""
    print("Mmmm let's see...")
    hogwarts()

hogwarts()
