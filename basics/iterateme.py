'''
Created on Apr 11, 2014

@author: vsa
'''

def play_iterator():
    s = 'Hello!'
    for c in s:
        print(c)
    
    it = iter(s)
    while(next(it)):
        print(it)
        
if __name__ == '__main__':
    play_iterator()