'''Create a class representing a concert ticket.
Its constructor takes two values: a ticket price,
and a section.

>>> my_ticket = ConcertTicket(22.0, 'floor')
>>> your_ticket = ConcertTicket(42.0, 'mezzanine')

You can access these two values through the price and section
attributes:

>>> my_ticket.price
22.0
>>> your_ticket.section
'mezzanine'

Once set, the price cannot be changed. If you try to set it,
it raises an error.

>>> my_ticket.price = 20.0
Traceback (most recent call last):
...
AttributeError: can't set attribute

The section can be changed, but can only be set to "floor", "lower",
"mezzanine", or "premier". If you try to change it to something
different, a ValueError is raised, with a descriptive error message:

>>> my_ticket.section = "lower"
>>> my_ticket.section
'lower'
>>> my_ticket.section = "premier"
>>> my_ticket.section
'premier'
>>> my_ticket.section = "upper_mezzanine"
Traceback (most recent call last):
...
ValueError: Invalid section "upper_mezzanine"

'''

# Write your code here:

class ConcertTicket(object):
    SECTIONS = {
        'floor',
        'lower',
        'mezzanine',
        'premier',
        }
    def __init__(self, price, section):
        self._price = price
        self._section = section
    @property
    def price(self):
        return self._price
    @property
    def section(self):
        return self._section
    @section.setter
    def section(self, value):
        if value not in self.SECTIONS:
            raise ValueError('Invalid section "{}"'.format(value))
        self._section = value

# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Copyright 2015-2017 Aaron Maxwell. All rights reserved.
