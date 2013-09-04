import unittest
import httplib
import urllib2

def basehttp(httpverb,uri,params=None):
    conn = httplib.HTTPConnection('foxcitieskidsdeals.appspot.com:80')
    conn.request(httpverb,uri,params)
    res = conn.getresponse()
    return res

class MyTests(unittest.TestCase):
    """
    def test_businesses(self):
        t = basehttp('DELETE','/businesses')
        self.assertEqual(t.status,200)
        t = basehttp('POST','/businesses','name=blee&deal=blah')
        self.assertEqual(t.status,200)
        self.assertIn('/business',t.read())
        t = basehttp('GET','/businesses')
        self.assertEqual(t.status,200)
    """
    def testbusinessesget(self):
        t = basehttp('GET','/businesses')
        self.assertEqual(t.status,200)
    def testbusinessesdelete(self):
        t = basehttp('DELETE','/businesses')
        self.assertEqual(t.status,200)
    def testbusinessespost(self):
        t = basehttp('POST','/businesses','name=Sergio\'s&deal=Sundays kids eat for $0.99&phone=9205551212&address=123 College Ave. Appleton WI 54911&category=ahRzfmZveGNpdGllc2tpZHNkZWFsc3IPCxIIQ2F0ZWdvcnkY0Q8M')
        self.assertEqual(t.status,200)
        res = urllib2.urlopen(t.read())
        self.assertIn('Sergio',res.read(),res.read())
    def testbusinessesput(self):
        t = basehttp('PUT','/businesses','name=Sergio\'s&deal=Sundays kids eat for $0.99&phone=9205551212&address=123 College Ave. Appleton WI 54911&category=ahRzfmZveGNpdGllc2tpZHNkZWFsc3IPCxIIQ2F0ZWdvcnkY0Q8M')
        self.assertEqual(t.status,501)



suite = unittest.TestLoader().loadTestsFromTestCase(MyTests)
unittest.TextTestRunner(verbosity=2).run(suite)
#[{"obj_key": "ahRzfmZveGNpdGllc2tpZHNkZWFsc3IPCxIIQ2F0ZWdvcnkY0Q8M", "name": "a"}]

