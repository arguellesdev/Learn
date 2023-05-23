"""We are defininig dictionaries with songs"""

def dict1():
    """songs of Shawn Mendes on different years"""
    song ={ "2018": ("fallin' all in you", "in my blood",
            "lost in japan"), "2022": ("when you're gone", "summer of love"), "2015": "stitches" , }
    print (song.keys())
    print ("before: ", song.values())
    year_18(song)
    year_20(song)
    changing_s(song)
    year_22(song)

def year_18(song):
    """songs of 2018"""
    print ("The songs of 2018 was:", song["2018"])

def year_20(song):
    """adding new songs"""
    song['2020'] = "monster"

def changing_s(song):
    """change new songs"""
    song['2022'] = ("when you're gone", "heartbeat", "summer of love")

def year_22(song):
    """"finding song"""
    find = input("which year is when you're gone: ".capitalize())
    if find == '2022':
        print ("you really like Shawn", song.values())
    else:
        del song['2022']
        print ("are you sure, is not here: ", song.values())
dict1()
