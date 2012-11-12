# Everything after the hash symbol is a comment
# Comments continue until the end of the line

# The % (modulo) is the string formatting, or interpolation operator.
# It takes the form >>> format % values
'%s' % 'Hello World'
message = 'The message "%s" is inserted here' % 'What\'s up?'
print message

# The %s format argument converts values to strings...
# As though it were called by str()
'%s' % 42
'%s' % True

class Actor(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

actor = Actor('John Cleese')
actor
'The actor %s, is tall.' % actor
print actor

# Multiple values are contained in tuples
'%s %s %s %s' % (message, 1939, False, actor)

# All arguments must be used
'%s %s' % (message, 1939, False, actor)

# Values can be contained in a single mapping object (e.g. a dict)
values = {
    'message': message, 
    'year': 1939, 
    'working': False, 
    'name': actor
    }

# And then referenced by name
'%(message)s %(year)s %(working)s %(name)s' % values

# Not all of these named arguments have to be used
'%(message)s' % values
'There is no formatting here' % values

# The %r format argument is used to return an object's representation...
# As though it were called by repr()
'%r' % actor
'The actor %s looks like %r' % (actor, actor)
'The actor %(name)s looks like %(name)r' % {'name': actor}

class Actor(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
    def __repr__(self):
        return '<Actor(%r)>' % self.name

actor = Actor('John Cleese')
'%r' % actor
        
# There are other formatting arguments, these are two common ones:
# %d an integer
'%d' % 15.59
# %f represents a float
'%f' % 15.59
'%(balance)f' % {'balance': 15.59}
from math import pi
'%f' % pi

# Minimum width
'%20f' % pi
# Padding (zero fill)
'%020f' % pi
# Conversion 
'%+f' % pi
'%+f' % (pi * -1)
# Precision
'%.10f' % pi
'%+020.10f' % pi

# The % operator will eventually be depreceated in favour of
# "new style" formatting via the str.format method using {}
# http://docs.python.org/2/library/string.html#formatspec
'{}'.format('New Style')

# Value arguments can be referenced by order
'{} {} {} {}'.format(message, 1939, False, actor)

# Value arguments can be referenced by position
'{3} {0} {2} {1}'.format(message, 1939, False, actor)

# But not both together
'{3} {} {} {1}'.format(message, 1939, False, actor)

# Values arguments can be referenced by name
'{name} is the name of the actor'.format(name=actor)

# Or both (all unnamed arguments must come before named)
'{name} {} {} {}'.format(message, 1939, False, name=actor)
'{name} {2} {1} {0}'.format(message, 1939, False, name=actor)

# Not all argument values have to be referenced in the format string
'{} {}'.format(message, 1939, False, name=actor)
'{2} {1}'.format(message, 1939, False, name=actor)
'{name}'.format(message, 1939, False, name=actor)

# And argument values can be referenced more than once
'{name} {1} {1} {1}'.format(message, 1939, False, name=actor)

# Attributes of objects can also be accessed
from datetime import date
actor.dob = date(1939, 10, 27)
'{0.name} was born on {0.dob}'.format(actor)
'{actor.name} was born on {actor.dob}'.format(actor=actor)
'{actor.name} was born in {actor.dob.year}'.format(actor=actor)

# List-type arguments expose their items
numbers = [2,4,6,8]
letters = ['a','b','c']
'{0[3]} {1[2]} {0[1]} {1[0]}'.format(numbers, letters)

# Parameters to the format method can be expanded
'{2} {1} {0}'.format(*letters) # Unnamed arguments
'{year}'.format(**values) # Named arguments
'{} {} {} {} {year}'.format('Arg0', 'Arg1', *letters, **values)

# An object's representation value is accessed by !r
'{!r}'.format(actor)
# (!s is also available, but not necessary as it's implied)
'{!s}'.format(actor)
'{}'.format(actor)

# Various formatting options passed after a colon: width, fill, alignment
'{:30}'.format('a small string')
'{:>30}'.format('a small string')
'{:<30}'.format('a small string')
'{:^30}'.format('a small string')
'{:=^30}'.format('a small string')
'{0.name:=^30}'.format(actor)

# Numeric formatting: precision, width, fill, alignment
'{:f}'.format(pi)
'{:.3f}'.format(pi)
'{:15.3f}'.format(pi)
'{:015.3f}'.format(pi)
'{:<015.3f}'.format(pi)

# Types can define their own custom formatters. Notably dates.
'{actor} was born on {actor.dob:%A %d %B, %Y}'.format(actor=actor)

# Using the comma as a thousands separator.
'{:,}'.format(1234567890)

# Expressing a percentage
'{:.2%}'.format(15.5/80)

# http://docs.python.org/2/library/string.html#format-specification-mini-language
