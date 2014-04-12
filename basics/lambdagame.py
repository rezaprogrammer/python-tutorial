'''
Created on Apr 11, 2014

@author: vsa
'''

def test_lambda():
    def f(n=1): return lambda x: x**n;
    for i in range(10):
        print(f(2)(i))


if __name__ == '__main__':
    test_lambda()
    pass