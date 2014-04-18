'''
Created on Apr 18, 2014

@author: vsa
'''

import threading, zipfile, os

class AsyncThread(threading.Thread):
    def __init__(self, infilename, outfilename):
        threading.Thread.__init__(self)
        self.infilename = infilename
        self.outfilename = outfilename
    
    def run(self):
        f = zipfile.ZipFile(self.outfilename, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infilename)
        f.close()

if __name__ == "__main__":
    # Create new thread
    infilename = "c:\\temp\\DSCF7075.jpg"
    filename, ext = os.path.splitext(infilename)
    filename = os.path.split(filename)[-1]
    outfilename = 'c:\\temp\\{0}.zip'.format(filename)
    t = AsyncThread(infilename, outfilename)
    t.start()
    t.join(1000)
    print('Done! Results written to {0}'.format(outfilename))
