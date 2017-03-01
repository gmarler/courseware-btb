'''Solve everything here using list comprehensions. Most can also be
solved with a regular for loop, but do NOT do that - only use list comprehensions.

Use multiple for clauses to build this list of tuples:

>>> pairs
[(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]

For the next batch, we'll use this test data:

>>> colors
['aquamarine', 'orange', 'teal', 'cyan']

>>> garments
['hat', 'belt', 'bell bottoms', 'cape', 'trench coat']

Create a new list comprehension called "combos", which is constructed from
"colors" and "garments".

>>> for combo in combos:
...     print(combo)
...
aquamarine hat
aquamarine belt
aquamarine bell bottoms
aquamarine cape
aquamarine trench coat
orange hat
orange belt
orange bell bottoms
orange cape
orange trench coat
teal hat
teal belt
teal bell bottoms
teal cape
teal trench coat
cyan hat
cyan belt
cyan bell bottoms
cyan cape
cyan trench coat

Now make a new list comprehension called "brief_combos". This one is a
different from the one above... what's being omitted?

>>> for combo in brief_combos:
...     print(combo)
...
aquamarine hat
aquamarine belt
aquamarine cape
orange hat
orange belt
orange cape
teal hat
teal belt
teal cape
cyan hat
cyan belt
cyan cape

'''

colors = ['aquamarine', 'orange', 'teal', 'cyan']

garments = ['hat', 'belt', 'bell bottoms', 'cape', 'trench coat']

# Write your code here:



# Do not edit any code below this line!


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Copyright 2015-2017 Aaron Maxwell. All rights reserved.
