# Everything after the hash symbol is a comment
# Comments continue until the end of the line

'Welcome to the quick introduction to Python talk at the Python North East User Group.' # A string literal is a *sequence* of bytes contained within single or double quotes.

print """
Welcome to the quick introduction to Python 
talk at the Python North East User Group.
""" # Strings can also be contained within triple single or triple double quotes to maintain whitespace.

message = 'Welcome to the quick introduction to Python talk at the Python North East User Group.' # Assigns to the "message" variable
print message

'Python' in message # We can check that an item is *in* a string
'PHP' in message
'Ruby' not in message # And check that an item is *not in* a string

# Strings are iterable
for letter in message:
    print letter

    
len(message) # Strings have a length

print message
message[6] # Items in a string can be copied using a zero-based index
message[-11] # Negative index values return items from the end of the string

# Strings are *immutable*. They cannot be changed *in place*.
message[0] = 'E'

# But strings can be copied to create new strings
real_message = " We've got pizza!" # Another string
real_message * 5 # String can be copied multiple times using the "*"

# Strings are concatenated using the "+" operator
full_message = message + real_message + " And, we've got drinks!"

print full_message

# Items in a string can be copied using *slices*.
# Slices are "from" and "to" index points separated by a ":".
message[56:73]
message[56:-12] # The "from" and "to" index values can be positive or negative.
message[-29:-12]

# By not providing a "from" or "to" index value, Python will continue until the end of the string.
message[:48]
message[0:48]
message[56:]
message[-29:]

message[56:73:1] # Slices also take a "steps" value after a 2nd ":"
message[56:73:3]
message[::4] # What's going to happen here?

message[0:7:0] # The *value* of a slice's step cannot be zero.

message[7:0:-1] # However, steps in a slice can be negative.

# By not providing "from" or "to" index values, Python will continue until the end of the string in the direction of the given steps
message[6::-1]
message[0::-1] # What would you expect here?
message[::-1] # What about here?

'This "%s" is the content of message' % message # Strings contain in-built formatting using the precent chracter

'This should be a number "%d"' % 1000 # You can specify the allowable value type

'This "%s" will be converted to a string' % 1000
# Python strings contain their own mini formatting language which would require their own talk!

dir(message) # Strings are first class objects with their own methods. 

# Some return copies of the string.
message.lower() # Call the "lower" method of a string
message.upper() # Call the "upper" method of a string
message.title() # Call the "title" method of a string
message.capitalize()# Call the "capitalize" method of a string

message.count('e') # Count the number or times 'e' occurs in the string

message.index('e') # Return the position of the first occurrance of 'e'

message.startswith('Welcome') # And some methods return boolean values
message.endswith('bye!')

# Some methods return instances of other sequence types.
message.split() # This returns a list, split on spaces
message.split('to') # This returns a list split on 'to'
