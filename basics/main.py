'''
Created on Apr 6, 2014

@author: reza
'''

from leeth import PolishExpression
from basics import fib

import leeth
from leeth.PolishExpression import evaluate_polish

def printout_something():
    print("Hi!")

def some_lambda_func(val):
    return lambda x: val * x

def test_lambda_func():
    f = some_lambda_func("Hello-");
    print(f(5))
    
def some_list_ops():
    L = []
    for x in range(1,5):
        L.append(x)
    
    for x in L:
        print(x)
        
    print(L)
    
def some_more_list_ops():
    L1 = [2*x for x in range(10)]
    print(L1)

    L2 = list(map(lambda x: 2*x, range(10)))
    print(L2)
    
    print(L1 == L2)
    print(L1.reverse() == L2)
    print(L1.reverse() == L2.reverse())

def transpose_matrix(m):
    t = []
    rows = len(m)
    if rows == 0:
        return t
    
    cols = len(m[0])
    for i in range(cols):
        t.append([row[i] for row in m])
    return t

def test_transpose_matrix():
    m = [[1,2,3],[10,20,30]]
    print(m)
    print
    print(transpose_matrix(m))
    
if __name__ == '__main__':
    
    #evaluate_polish(expr)
    #print(40 * 'x')
    
    #test_lambda_func()
    
    #some_list_ops()
    #some_more_list_ops()
    #test_transpose_matrix()
    
    # Polish expressions
    #stack = [10, 2, '+']
    #res = evaluate_polish(stack)
    #print(res)
    
    # Fibonacci
    print(fib.fibbonacci(50))
    
    pass
