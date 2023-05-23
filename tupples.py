"""In this document we are creating tupples in order to understand the inmutable concept,
and no, is not because you talk a lot haha"""
    # pylint: disable=invalid-name
    # "python.linting.pylintArgs": ["--disable=C0103"]

def main_2():
    """defining main tupple to create new chaos, you are welcome ;)"""
    tuple1 = ('ACDC', 'War machine', 1986)
    print (tuple1)
    identify(tuple1)
    terminator(tuple1)
    sara_connor(tuple1)

def terminator(tuple1):
    """metaverse chaos, defining more chaos"""
    tuple1 = list(tuple1)  # Convert the tuple to a list
    tuple1[2] = str(tuple1[2])
    print(type(tuple1[2]))
    # print(type(tuple1[-1]))
    print("The year was:".title(), tuple1[2])

def identify(tuple1):
    """identifying chaos, hello dear inmutable stuff, no worries I'll clone you"""
    print(type(tuple1[2]))
    # print(type(tuple1[-1]))
    print("The year was:".title(), tuple1[2])

def sara_connor(tuple1):
    """Let's Connor put some sugar or kill u, it is up to you"""
    print(len(tuple1))
    s= 2008
    tuple2 = tuple1[0:2] + (s,)
    #When we write (S,) with a comma after the S, we are creating a one-element tuple in Python.
    # The reason for the comma is that when we define a tuple with only one
    # element, Python treats it as a regular value, not a tuple.
    print(tuple2)
    print (len(tuple2))

main_2()
