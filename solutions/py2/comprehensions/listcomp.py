'''To start, define a few number lists. Be sure to create each one
with a list comprehension; don't use a for loop. Use range() for the
base sequence.

>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64]

>>> cubes
[0, 1, 8, 27, 64, 125]

>>> squares_of_evens
[0, 4, 16, 36, 64]

Next, define a function called "palindromes" that takes a list of
strings as input, and (using a list comprehension) constructs and
returns a list of palindromes.  (A palindrome is a string that is the
same backwords and forwards, like "abccba". Hint: in Python, the
reverse of a string "s" is written "s[::-1]".)

>>> palindromes(["foo", "bar"])
['foooof', 'barrab']

>>> palindromes(["ab", "cat", "q", "qq"])
['abba', 'cattac', 'qq', 'qqqq']

>>> palindromes(["abc", "xyz"])
['abccba', 'xyzzyx']

Here are some name lists:

>>> names = ["Albert", "Fred", "Amanda", "Tim", "Joe", "Aaron"]
>>> names2 = ["George", "Gus", "Aaron", "Ted", "Gina"]

Write a function "starting_with" that gives you names starting with a
certain letter. Its body should just have a return statement,
returning a list comprehension.

>>> starting_with("A", names)
['Albert', 'Amanda', 'Aaron']
>>> starting_with("F", names)
['Fred']
>>> starting_with("G", names2)
['George', 'Gus', 'Gina']
>>> starting_with("A", names2)
['Aaron']

Make it case-insensitive too:
>>> starting_with("a", names)
['Albert', 'Amanda', 'Aaron']
>>> starting_with("g", names2)
['George', 'Gus', 'Gina']

'''

# Write your code here:

squares = [ n**2 for n in range(9) ]
cubes = [ n**3 for n in range(6) ]

squares_of_evens = [
    square for square in squares
    if square % 2 == 0
]

def palindromes(items):
    return [ item + item[::-1]
             for item in items ]

def starting_with(letter, words):
    return [
        word for word in words
        if word.lower().startswith(letter.lower())
    ]
# Do not edit any code below this line!


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Copyright 2015-2017 Aaron Maxwell. All rights reserved.
