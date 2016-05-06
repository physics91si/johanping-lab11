import numpy as np

#Squares: Create a list of the first 10 square numbers. First use a list comprehension, then use a
#lambda function and map

#list comprehension
num_list = np.arange(1,11)
squares = [number**2 for number in num_list]
print(squares)

#map
print(list(map(lambda num: num**2, num_list)))

from functools import reduce

#Products: Use a lambda function with reduce to multiply up the numbers from 1 to 5.
one_to_five = np.arange(1,6)
reduce(lambda x,y: x*y, one_to_five)

# Filenames: Say that you have a string with a list of file names "test1.py	test2.py	
# Physics 91SI Spring 2016
# 2
# test3.py	..." and you want to output a list of just the filenames without the .py extension.
# Do this with a list comprehension.
files = ['test1.py', 'test2.py', 'test3.py']
[name[:name.index('.py')] for name in files]

# Dictionary, which takes a string (ex: "Spam	and	eggs	should	not	have	legs!") and
# returns a set of the unique words, case-insensitive.
string = "Spam and eggs should not have legs!"
[word if (list.index(word)!= list) for word in string]

import matplotlib.pyplot as plt

dict = {1:1, 2:4, 3:9, 4:16, 5:25, 6:36, 7:49, 8:64, 9:81, 10:100}
[plt.plot(item) for item in dict]
