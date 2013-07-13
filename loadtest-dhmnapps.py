from threading import Thread
from httplib import HTTPConnection

class URLThread(Thread):
    def __init__(self):
        super(URLThread, self).__init__()
    def run(self):
        for req in range(reqsperthread):
            conn = HTTPConnection(host='dhmnapps.appspot.com',timeout=30)
            conn.request('GET','/')
#usage: host path 
reqsperthread = 100 
numberofthreads = 10 
for athread in range(numberofthreads):
    print athread,
    thread = URLThread()
    thread.start()
