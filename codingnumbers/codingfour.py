"""In this section we are going to learn recursvity with simple condiotionals"""

def dark():
    """talk about it"""
    x_v= input("what is x? ")
    if x_v.isnumeric():
        x_v = float(x_v)
        print(x_v)
    y_v = input ("what is y?")
    if y_v.isnumeric():
        y_v = float (y_v)
        print(y_v)
    if x_v != y_v:
        #if x_v > y_v or x_v < y_v:
        print("welcome nerdy". capitalize())
        z_v = y_v ** x_v
        print(f"{float(z_v):,f}")
    else:
        print ("x is equal to y, enter a valid x".capitalize())
        return dark()
dark()
        