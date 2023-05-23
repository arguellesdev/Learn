"""splitting simple way"""
def main():
    """defining a_list"""
    a_list = ["Anya Arguelles", 5, 4, 1986]
    # My name with my born date
    print(a_list)
    split_2(a_list)
    print(a_list)

def split_2(a_list):
    """splitting"""
    B = input('enter your name: ').title().split(',')
    print(B)
    # Separa los elementos
    a_list.extend(B)

main()
