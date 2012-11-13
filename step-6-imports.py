# Python North East
# 'import' and namespacing

# In Python we have some built-in functions and variables:

print('This function is always available!')

# We can see what is locally available using 'dir'
print dir()

airspeed_velocity_unladed_swallow = '24mph'
# ref: http://style.org/unladedswallow/

print dir()

# The majority of things need to be 'imported'

# 'os' is one of the standard modules available 
import os

# Now, we have an object in our local namespace called 'os'
print os

# Notice that this isn't like PHP or Ruby where require/include pulls things
# directly into the local namespace. Modules are always run 'once', unlike
# PHP's 'include'. It's a bit like Java's import though.

# This is a module object, and it can contain functions, variables etc.,
print os.getcwd()

# We can also pull individual pieces out of a module into our local namespace
from os import getcwd
# This is now local!!!
getcwd()
print dir()

# You can import EVERYTHING from a module like this:
from os import *

# But try and avoid this as it fills your local namespace :)
print dir()

# This makes me a SAD panda
# ...honestly, don't do this unless you have a good reason.

# Another example: 
from datetime import date

print date.today()

# Python has a great standard library, it's 'batteries included'.
# See http://docs.python.org/library/

# Packages are groupings of modules. Sub-modules are separated with a '.' 

import xml.sax.saxutils

# Note the full namespace is 'xml.sax.saxutils'
print xml.sax.saxutils.escape('<p>Some nasty html</p')

# We can import a submodule:
from xml.sax import saxutils
print saxutils.escape('<h1>More nasty HTML</h1>')

# And objects directly from the submodule too
from xml.sax.saxutils import escape
print escape('<p>You get the idea...</p>')

# I've not discussed how to make modules or where Python looks for them - both
# topics are quite simple  In short, modules are just .py files or folders 
# with a special file '__init__.py' in the route of the folder
# As for where Python looks for modules:

import sys
print sys.path
# And we can even edit it if we want to
sys.path.append('/a/new/place/for/modules')

# Now to wrap up and hammer home that point about from <blah> import *
import webbrowser
webbrowser.open('http://www.youtube.com/watch?v=I6vPRaIrvqU')

# Questions?
