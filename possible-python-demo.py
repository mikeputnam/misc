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
print "p.data.get('legalname',None)  :", p.data.get('legalname',None)
print "p.data.get('fakedata',None)  :", p.data.get('fakedata',None)

if p.data.get('fakedata',None):
    print "person has "
else:
    print ""
