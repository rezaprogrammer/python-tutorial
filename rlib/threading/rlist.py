'''
Created on Apr 20, 2014

@author: vsa
'''

from threading import Lock
from threading import Thread

class RList:
    '''This class implements a thread safe list.'''
    
    def __init__(self):
        self.lock = Lock()
        self.list = []
    
    def append(self, v):
        '''Appends element 'v' to the list.'''
        
        self.lock.acquire()
        try:
            self.list.append(v)
        finally:
            self.lock.release()
    
    def pop(self):
        '''Pops the last element in the list.'''
        
        self.lock.acquire()
        try:
            v = self.list.pop()
        finally:
            self.lock.release()
        return v
    
    def size(self):
        '''Returns the number of elements in the list.'''
        
        self.lock.acquire()
        try:
            s = self.size()
        finally:
            self.lock.release()
        return s

class RListTesterThread(Thread):
    '''A simple tester class for RList.'''
    
    def __init__(self, id, rlist, n):
        Thread.__init__(self)
        self.id = id
        self.rlist = rlist
        self.n = n
    
    def run(self):
        while self.n>0:
            self.n = self.n-1
            self.rlist.append(self.n)
            m = self.rlist.pop()
            if(self.n!=m):
                print('{0}: {1}!={2}'.format(self, self.n, m))
        pass
    
    def __repr__(self):
        return str(self.id)
    
if __name__ == '__main__':
    n = 1000
    m = 10000
    rlist = []
    tlist = []
    for i in range(n):
        t = RListTesterThread(i, rlist, m)
        tlist.append(t)
        t.start()
    pass