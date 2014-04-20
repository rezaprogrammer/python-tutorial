'''
Created on Apr 11, 2014

@author: vsa
'''

def play_iterator():
    s = 'Hello!'
    for i, c in enumerate(s):
        print('{0} -> {1}'.format(i, c))
    
    it = iter(s)
    while(next(it)):
        print(it)
        
if __name__ == '__main__':
    play_iterator()