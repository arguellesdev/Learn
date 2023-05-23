"""readline() method only reads the first line of a file"""
with open("Example1.txt","r") as file1:
    file_stuff= file1.readline()
    print(file_stuff)
import numpy as np
a=np.array([0,1,0,1,0])
b=np.array([1,0,1,0,1])
c = a*b
print (c)