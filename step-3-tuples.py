# Tuples are similar to lists. We use ( ) to create them
x = (1, 2, 3)
print x

# vs [1, 2, 3]
list_x = [1, 2, 3]

# Watch out for 
(1) != (1,)

# Single element tuples MUST be terminated with a comma
# This trips beginners up quite a lot

# We can read them much as we read lists
print len(x)

# Access by index
print x[1]

# Slice
print x[1:]

# Iterate
for i in x:
    print i

# Unpack
a, b, c = x

print a
print b
print c

# ... you get the idea!
# However, tuples are _immutable_, i.e. they cannot be altered

# can't erase elements!
del x[1]

# can't add new elements
x.append(5)

# So why have (1, 2, 3) when we can have [1, 2, 3]
# Throw to the audience...

# 1. Because they're much more efficient
# 2. Because immutability reinforces the simplicity of the data they hold
# 3. Because we can use them as keys for dicts, e.g.

my_dict = {(42,1): 'value'}

# You can easily convert tuples to lists (or any thing you can iterate
# over) with list()

my_list = list(x)

