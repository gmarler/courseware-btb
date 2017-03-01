'''
Ohm's law is a simple equation describing electrical circuits. It
states that the voltage V through a resistor is equal to the current
(I) times the resistance:

V = I * R

The units of these are volts, ampheres (or "amps"), and ohms,
respectively. In real circuits, often R is actually measured in
kiloohms (10**3 ohms) and I in milliamps (10**-3 amps).

Let's create a Resistor class that models this behavior. The
constructor takes two arguments - the resistance in ohms, and the
voltage in volts:

>>> resistor = Resistor(800, 5.5)
>>> resistor.resistance
800
>>> resistor.voltage
5.5

The current is derived from these two using Ohm's law:
(Hint: use @property)

>>> resistor.current
0.006875

Since we may want the value in milliamps, let's make another property
to provide that:

>>> resistor.current_in_milliamps
6.875

Let's set it up so that we can change the current, and doing so will
correspondingly modify the voltage (but keep the resistance constant).

>>> resistor.current_in_milliamps = 3.5
>>> resistor.resistance
800
>>> round(resistor.voltage, 2)
2.8
>>> resistor.current = .006875
>>> round(resistor.voltage, 2)
5.5
>>> resistor.resistance
800

Also, we've made a design decision that a Resistor cannot change its
resistance value once created:

>>> resistor.resistance = 8200
Traceback (most recent call last):
AttributeError: can't set attribute

'''

# Write your code here:

class Resistor(object):
    def __init__(self, resistance, voltage):
        self._resistance = resistance
        self.voltage = voltage

    @property
    def resistance(self):
        return self._resistance

    @property
    def current(self):
        return self.voltage / self.resistance

    @current.setter
    def current(self, value):
        self.voltage = self.resistance * value

    @property
    def current_in_milliamps(self):
        return self.current * 1000

    @current_in_milliamps.setter
    def current_in_milliamps(self, value):
        self.current = value / 1000

# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Copyright 2015-2017 Aaron Maxwell. All rights reserved.
