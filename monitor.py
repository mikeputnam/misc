import select
from select import kqueue, kevent
import os
import sys
 
filename = "togglefile-flip"
fd = os.open(filename,os.O_RDONLY)
kq = kqueue()
 
event = [
    kevent(fd, 
           filter=select.KQ_FILTER_READ,
           flags=select.KQ_EV_ADD),
    kevent(fd, 
           filter=select.KQ_FILTER_VNODE,
           flags=select.KQ_EV_ADD | select.KQ_EV_CLEAR,
       fflags=select.KQ_NOTE_DELETE | select.KQ_NOTE_RENAME)
]
 
events = kq.control(event,0,0)
 
while True:
    r_events = kq.control(None,4)
    #for event in r_events:
    for event in r_events:
        if event.fflags & select.KQ_NOTE_DELETE:
            print "file was deleted"
        elif event.fflags & select.KQ_NOTE_RENAME:
            print "file was renamed"
            
kq.close()
os.close(fd)
