'''
Created on Apr 24, 2014

@author: vsa
'''
import unittest
import time

from threading import RLock

from async.runner import AsyncRunner
from async.runner import AsyncRunnerState

class Listener(object):
    
    def __init__(self):
        self._lock = RLock()
        self._received = []
        return
        
    def received(self, item):
        print('Received: {0}.'.format(item))
        self._lock.acquire()
        self._received.append(item)
        self._lock.release()
        return
    
    def received_count(self):
        self._lock.acquire()
        c = len(self._received)
        self._lock.release()
        return c
    
    def received_items(self):
        self._lock.acquire()
        r = self._received[:]
        self._lock.release()
        return r

class AsyncRunnerTester(AsyncRunner):
    
    def __init__(self, l):
        AsyncRunner.__init__(self)
        if not isinstance(l, Listener):
            raise Exception('Expected a Listener; got a {0}'.format(l.__class__))
        self._l = l
        return
        
    def execute(self, item):
        super(AsyncRunnerTester, self)
        self._l.received(item)
        return

class TestRunner(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        super(TestRunner, self).__init__(*args, **kwargs)
        self._lock = RLock()
        self._received = []
        
    def testRunner(self):
        listener = Listener()
        r = AsyncRunnerTester(listener)
        assert r._state == AsyncRunnerState.UNINITIALIZED
    
        r.initialize()
        assert r._state == AsyncRunnerState.INITIALIZED
        
        r.start()
        assert r._state == AsyncRunnerState.RUNNING

        input_items = ['item1', 'item2', 'item3']        
        for item in input_items:
            r.append(item)
        
        N = 3
        received_items = []
        while N > 0 and len(received_items) != 3:
            time.sleep(1)
            received_items = listener.received_items()
            print('{0}'.format(received_items))
            N = N - 1
        assert len(received_items) == 3
        for item in received_items:
            assert item == input_items.pop()
        
        r.stop()
        assert r._state == AsyncRunnerState.FINISHED
        
        return
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testRunner']
    #unittest.main()
    t = TestRunner()
    t.testRunner()