"LET'S CONSIDER LOOPS"

def repeat():
    """whatever las tortas. Repeats a string a number of times based on user input."""
    in_num = int(input("insert a number of meows here: "))
    while in_num > 0:
        # the way while loop works is that the python interpeter
        # just back and forth asking the question again and again
        for i in range(in_num):
            print("meow", i + 1)
            #in the previous case += operator is an assignment operator,
            # which means it is used to assign a new value to a variable.
            # It cannot be used within a function call, such as print().
            in_num -=1 #this can not be written on a print
            #The reason why in_num -=1 is necessary in the code is because it's being used
            # to decrement the value of in_num inside the while loop.
            # Without this line of code,the while loop will continue to execute indefinitely
            # since the condition in_num > 0 will always be true
            # In the previous code, the expression in_num -= 1
            # is a shorthand for "decrement in_num by 1".
            # It's equivalent to writing in_num = in_num - 1, but with fewer characters.
    if in_num <= 0:
        print("really? zero?? you need love")

repeat()
