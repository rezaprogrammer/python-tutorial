'''
Created on Apr 24, 2014

@author: vsa
'''

from threading import Thread, Condition
from threading import RLock
from enum import Enum

class AsyncRunnerState(Enum):
    UNINITIALIZED = 0
    INITIALIZED = 1
    RUNNING = 2
    FINISHED = 3
    
class AsyncRunner(object):
    '''
    classdocs
    '''
    
    __QUEUE_LOCK_RETRY = 10

    def __init__(self):
        '''
        Constructor
        '''
        self._state = AsyncRunnerState.UNINITIALIZED
        self._queue = None
        self._queue_lock = None
        self._queue_empty = None
        self._thread = None
    
    def initialize(self):
        if self._state != AsyncRunnerState.UNINITIALIZED:
            raise Exception('Wrong state: {0}.'.format(self._state))
        
        self._state = AsyncRunnerState.INITIALIZED
        self._thread = Thread(target = self.run)
        self._queue = []
        self._queue_lock = RLock()
        self._queue_empty = Condition(self._queue_lock)

    def start(self):
        if self._state != AsyncRunnerState.INITIALIZED:
            raise Exception('Wrong state: {0}.'.format(self._state))
        
        self._state = AsyncRunnerState.RUNNING
        self._thread.start()
        
    def append(self, item):
        self._queue_lock.acquire()
        self._queue.append(item)
        self._queue_empty.notify()
        self._queue_lock.release()
        
    def run(self):
        while self._state == AsyncRunnerState.RUNNING:
            self._queue_lock.acquire()
            item = None
            if len(self._queue) == 0:
                self._queue_empty.wait(AsyncRunner.__QUEUE_LOCK_RETRY)
            else:
                item = self._queue.pop()
            self._queue_lock.release()

            if item is not None:
                self.execute(item)
        
    def stop(self):
        if self._state is not AsyncRunnerState.RUNNING:
            raise Exception('Invalid state: {0}.'.format(self._state))
        self._state = AsyncRunnerState.FINISHED
        self._queue_lock.acquire()
        self._queue_empty.notifyAll()
        self._queue_lock.release()

    def execute(self, item):
        self.item = item
