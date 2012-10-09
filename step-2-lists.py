# The list datatype is one of the most used datatypes in Python
# Its also one of the easiest to understand
# It simply represensts a collection of items
# That can be added to or removed from.
# Items are refereced by their position in the list,
# called their Index.

[5, 6, 3, 8, 99, 105]  # A list is a sequence of items

x = [5, 6, 3, 8, 99, 105]  # Assigns a list to a variable

print x

print x[0]  # Gets a single item from list at index 0 ie. first element

print x[5]  # Gets items at index 5

x[5] = 666  # Reassign an element

print x

x.append(34)  # Adds item to end of list

print x

x.append('oranges')  # You can mix datatypes

print x

x[2] = 3.141

print x

nother_list = ['a', 'b', 'c']  # Define another list

print nother_list

x[3] = nother_list  # Add to the list at index 3

print x

print x[0:4]  # shows elements from 0 till before element 4

print x[-2:]  # shows last two elements

c = x  # Assigns the list to new variable

print c

c[0] = 'changed'

print c

print x  # The list x has changed as well

x[0] = 55

print c  # The two variables are pointing to same list

c = x[:]  # Saying we want all elements which makes a copy

c[0] = 'changed'

print c

print x

print nother_list  # What about copying lists within lists

nother_list.append('wowsers')

print c

nother_list.pop()  # Removes last item in list

import copy

c = copy.copy(x)  # Same as [:]

c = copy.deepcopy(x)  # makes a copy of all elements and subelements

nother_list.append('wowsers')

print nother_list

print c


def hello_world():
    #This function on execution returns string 'hello world'
    return 'hello world'

c[0] = hello_world()  # Assigns result of function call to element 0

print c

c[0] = hello_world  # This assigns the actual function to element 0

print c

print c[0]()  # Calls the function
