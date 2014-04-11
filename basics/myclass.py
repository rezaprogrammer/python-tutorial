'''
Created on Apr 11, 2014

@author: vsa
'''

class MyBaseClass():
    ''' This is my base class.'''
    
    def __init__(self):
        print(str(self) + '::' + '__init__()')
        pass
    
    def __str__(self):
        return 'MyBaseClass'
    

class MyClass(MyBaseClass):
    '''This is my class that is subclassed from my base class.'''
    
    def __init__(self):
        print(str(self) + '::' + '__init__()')
        
    def __str__(self):
        return 'MyClass'

if __name__ == '__main__':
    mbc = MyBaseClass()
    print(mbc)
    
    print('*' * 10)
    
    mb = MyClass()
    print(mb)