# Everything after the hash symbol is a comment
# Comments continue until the end of the line

# A dict ('dictionary') is a list of keys with associated values
my_dict = {
    'a': 'aardvark',
    'key': 'value'
}

# (it's basically a list of pairs, the key and value separated
# by a colon ':' and each pair separated by a comma ','
online_dict = {'a': 'aardvark', 'b': 'baal'}

# (It should look VERY familiar to users of Javascript)

# We access the value using [] syntax
print my_dict['key']

# We can add new key / values pairs to after the initial
# declaration
my_dict['hello'] = 'world'
print 'hello'

# A key can be a string, a number, or even a tuple:
my_dict[510] = 'AA55'
print my_dict[510]

my_dict[(1, 2)] = 'a value'
print my_dict[(1, 2)]

# Values can be _anything_ at all in the language

# Other containers are fine too, including other dicts
multi_dict = {
    'list': [1, 2, 3, 4],
    'dict': {'key': 'value'}
}

# This means you can create nested structures:

nested_dict = {
    'result': {
        'error_code': 0,
        'text': 'This is an example',
        'data': {
            'news-items': [1, 2, 3],
            'titles': ['test', 'titles'],
        }
    }
}

# Let's get news item number 2

print nested_dict['result']['data']['news-items'][1]

# And you're not just limited to data either, how about code?

# Create an empty dict
func_dict = {}


# Create a function that says 'hello'
def say_hello():
    print 'hello!'

# Assign the function to a key in the dict
func_dict['my_function'] = say_hello
func_dict['my_function']()

# We test to see if a key is set with 'in':

'hello' in my_dict
'I am not a key' in my_dict

# We can remove a key with the 'del' keyword
del my_dict['hello']
print my_dict['hello']

# (Note how that threw an error - we have several ways
# of doing a 'safe' fetch from a dict)

if 'hello' in my_dict:
    value = my_dict['hello']
else:
    value = 'default value'

# (single line version of the above)
value = my_dict['hello'] if 'hello' in my_dict else 'default_value'

# Exception handling:

try:
    value = my_dict['hello']
except KeyError:
    value = 'default value'

# Better still, use the 'get' method on dicts
value = my_dict.get('hello', 'default_value')


# We can iterate over all keys and values very easily
for key, value in my_dict.items():
    print 'Key value pair: %s=%s', (key, value)

# Or just iterate over the keys
for key in my_dict:
    print key

# Ssh... a little secret
# Dicts are used by Python itself to store values on classes, functions and
# modules. You can do some scary stuff playing with these, but that is
# beyond the scope of today
