'''
Created on Apr 9, 2014

@author: vsa
'''
def fibbonacci(n):
    a = 1
    b = 1
    for i in range(n-1):
        a, b = b, a+b
    return a


if __name__ == '__main__':
    for i in range(10000):
        print(i, fibbonacci(i))