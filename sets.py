"""LOL Welcome to setting entrophy SETS are also a type of collection.
    Sets are a type of collection. This means that like lists and tuples,
    you can input different Python types. Unlike lists and tuples, they are unordered."""

def coffee_list():
    """what are the coffee brands u used to drink"""
    coffeetype= ["foldgers", "bulletproof", "yuban", "cafe central", "cincelar",
                 "dunkin", "dunkin", "caffenio"]
    print (type(coffeetype))
    print (coffeetype)
    set_c(coffeetype)

def set_c(coffeetype):
    """setting stuff"""
    coffee_set = set(coffeetype)
    coffeelocal={"cafe central", "cincelar", "caffenio", "cafe combate", "aphoteca"}
    coffee_set = coffee_set.union(coffeelocal)
    print (type(coffee_set))
    add_cof(coffee_set) #mutable
    print (coffee_set)
    print('The difference is: ', coffee_set.difference(coffeelocal))
    print('The mutual coffees are: ', coffee_set.intersection(coffeelocal))

def add_cof(coffee_set):
    """which one you like"""
    add_coffee = input('What type of coffee you drink: ')
    if add_coffee not in coffee_set:
        coffee_set.add(add_coffee) #adding a coffee
    else:
        print ('your coffee is already on the normal list')
    # check if add_coffee is a subset
        if {add_coffee}.issubset(coffee_set):
            print(f"{add_coffee} is a subset of coffee_set")
        else:
            print(f"{add_coffee} is NOT a subset of coffee_set")

coffee_list()
