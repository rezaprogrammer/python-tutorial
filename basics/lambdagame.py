'''
Created on Apr 11, 2014

@author: vsa
'''

def test_lambda():
    def f(n=1): return lambda x: x**n;
    for i in range(10):
        print(f(2)(i))

def test_map():
    def f(n): return lambda x: n**x
    l = list(range(10))
    for i in range(10):
        print(map(f(i), l))

def test_sets():
    s = {3,1,2,1}
    print(s)
    
if __name__ == '__main__':
    #test_lambda()
    #test_map()
    test_sets()
    pass