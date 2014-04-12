'''
Created on Apr 11, 2014

@author: vsa
'''

import unittest
from timeit import Timer

class TestMe(unittest.TestCase):
    def test_me(self):
        for i in range(10):
            print('Testing {0}'.format(i))
            
    def test_you(self):
        t = Timer('t=a; a=b; b=t', 'a=10; b=20').timeit
        print(t)
        
    pass

unittest.main()