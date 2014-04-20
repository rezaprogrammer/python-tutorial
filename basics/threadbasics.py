'''
Created on Apr 18, 2014

@author: vsa
'''

import threading, zipfile, os
import logging
from enum import Enum

__all__ = "AsyncThread"

class AsyncThreadState(Enum):
     UNINIT = -1
     INIT = 0
     RUNNING = 1
     FINISHED = 2
 
class AsyncThread(threading.Thread):
    def run_uninit(self):
        print('This should not have happened: {0}'.format(self))
        
    def run_init(self):
        self.status = AsyncThreadState.RUNNING
        logging.info('Running the async thread {0}'.format(self.id))
        f = zipfile.ZipFile(self.outfilename, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infilename)
        f.close()
        self.status = AsyncThreadState.FINISHED
        logging.info('Finished running the async thread {0}'.format(self.id))

    def run_running(self):
        logging.error('Cannot run while running: {0}'.fomrat(self))
    
    def run_finished(self):
        logging.error('Cannot run while finished: {0}'.format(self))
    
    idcounter = 0
    morphosis = {AsyncThreadState.UNINIT: run_uninit,
                 AsyncThreadState.INIT: run_init,
                 AsyncThreadState.RUNNING: run_running,
                 AsyncThreadState.FINISHED: run_finished
                 }
    
    def __init__(self, infilename, outfilename):
        self.status = AsyncThreadState.UNINIT
        threading.Thread.__init__(self)
        self.infilename = infilename
        self.outfilename = outfilename
        AsyncThread.idcounter += 1
        self.id = AsyncThread.idcounter
        self.status = AsyncThreadState.INIT
        logging.info('Creating an async thread {0}'.format(self.id))
    
    def run(self):
        AsyncThread.morphosis[self.status](self)
        
    def __str__(self):
        return 'AsyncThread {0} in state {1}'.format(self.id, self.status)
    
if __name__ == "__main__":
    # Create new thread
    infilename = "c:\\temp\\DSCF7075.jpg"
    filename, ext = os.path.splitext(infilename)
    filename = os.path.split(filename)[-1]
    outfilename = 'c:\\temp\\{0}.zip'.format(filename)
    t = AsyncThread(infilename, outfilename)
    t.start()
    t.join(1000)
    print('Done!')
