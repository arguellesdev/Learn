"""chatgpthelp"""
def hogwarts():
    """defining name"""
    input_name = str(input("What is your name? "))
    print(input_name)
    return hat(input_name)

def gryffindor(input_name):
    """defining house"""
    app_names = ["hermione", "ron", "anya", "harry"]
    #add more if necessary
    if input_name.lower() in app_names:
        print((f"Welcome to Gryffindor, {input_name.title()}!").title())
        # print(("Welcome to Gryffindor, %s!" %input_name).title())
    else:
        print(f"interesting not Gryffindor, {input_name.title()}, let's find your house")
        slytherin(input_name)

def slytherin(input_name):
    """Slytherin house definition"""
    app_names = ["draco", "heinie"]
    if input_name.lower() in app_names:
        print ((f"Welcome to slytherin, {input_name}!").title())
    else:
        print ("Mmmmm... maybe you are not from Hogwarts")

def hat(input_name):
    """defining house if not gryffindor"""
    print("Mmmm let's see...")
    gryffindor(input_name)

hogwarts()
