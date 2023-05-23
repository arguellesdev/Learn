"""definiendo loops Loops Sometimes, you might want to repeat a given operation many times.
Repeated executions like this are performed by loops. We will look at two types of loops,
for loops and while loops."""

def redwine():
    """defining what brands of red wine we have at store"""
    brand = ['LA Cetto', 'Santo Tomas', '4S', "D'Aquino", 'Louis Jadot']
    print(len(brand))
    ittomex(brand)
    mexcounts(brand)
    for i, brand in enumerate(brand):
        print (i, brand)
def mexcounts(brand):
    """only Mexico wines"""
    i = 0
    name = brand[0]
    while name !="D'Aquino" and i == "Vena Cava":
        i= i + 1
        name=brand[i]
        print (brand)
    print ("It took", i, "repetitions to get out of loop")
    return brand

def ittomex(brand):
    """converting Italian wine to Mexico where vena cava bought brands"""
    for i in range(3, 5):
        # print("Before square ", i, 'is',  brand[i])
        brand[i] = 'Vena Cava'
        # print("After square ", i, 'is',  brand[i])
    return brand
redwine()