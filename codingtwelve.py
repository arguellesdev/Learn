"""using match built in function"""

def introducing():
    """introduce yourself"""
    name = str(input("What is your name?  ").title())

    match name:
        # case "Harry", "Hermione", "Ron": is WRONG code
        # In the match statement, the | operator
        # is used to combine multiple cases into one.
        # This operator is used to specify multiple patterns
        # that should be matched with the same action.
        #In this case, we want to match the values "Harry",
        #"Hermione", and "Ron" with the same action.
        case "Harry"| "Hermione"| "Ron":
            print ("Gryffindor")
        case "Draco":
            print ("Slytterin")
        case _:
            # the underscore case _: is a wildcard case, which matches any value
            # that did not match any of the previous cases.
            # It's similar to an else statement in an if-else block.
            input("Mmmm interesting, you are a mystery...What was your name? ")

introducing()

    # def introducing():

#     """introduce yourself"""
#     name = print(str(input("What is your name dear? ".title())))

#     match name:
#         case "harry", "hermione", "Ron":
#             print ("Gryffindor")
#         default:
#             print ("Mmmm interesting, you are a mystery...")
