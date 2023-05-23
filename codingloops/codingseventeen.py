"""basic knowledge for loops"""

# def main():
#     """dance dance dance merlina"""
#     dance(3)

# def dance(n):
#     """declaring conditions"""
#     name_in = input(str("What is your name "))
#     for _ in range(n):
#         print ("dance, " + name_in.capitalize())

def main():
    """basic knowledge for loops"""
    number = get_number()
    dance(number)

def dance(n):
    """declaring conditions"""
    name_in = input(str("What is your name "))
    for i in range(n):
        if i == n - 1:
            print ("dance, " + name_in.capitalize())
        else:
            print("dance, ")

def get_number():
    """number of times"""
    while True:
        n = input("What is n? ")
        if n.isdigit() > 0: #indicando que debe ser un valor positivo
            n = int(n)
            break
    return n

main()
