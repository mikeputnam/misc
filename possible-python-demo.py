"""
A demonstration of the Python programming language.
"""

class Person:
    """A person object"""
    def __init__(self):
        self.data = {}

p = Person()

p.data = {"legalname":"John Doe","eyecolor":"brown","typeofperson":"worker"}

print "p.__doc__    :", p.__doc__
print "p.data   :", p.data
print "p.data['legalname']  :", p.data['legalname']
