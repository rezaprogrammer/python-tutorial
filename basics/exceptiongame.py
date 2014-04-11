'''
Created on Apr 10, 2014

@author: vsa
'''

class MyExceptionGame(Exception):
    '''A game over exception!'''
    
    def __init__(self):
        pass
    
    def __str__(self):
        return repr("Game over!")
    
def try_raising_exception():
    try:
        raise MyExceptionGame()
    except MyExceptionGame as my_ex:
        print('Just caught an exception {0}'.format(my_ex))

if __name__ == '__main__':
    try_raising_exception()