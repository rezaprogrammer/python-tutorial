'''
Created on Apr 10, 2014

@author: vsa
'''
import json

def read_some_file(filename):
    print('Reading file: {0}'.format(filename))
    f = file(filename, 'r')
    for l in list(f):
        print(json.dumps(l))
    pass

def read_some_file_differently(filename):
    with open(filename, 'r') as f:
        for l in f.readlines():
            print(l)
            
        pass

def test_some_file():
    filename = "c:\\temp\\a.txt"
    try:
        read_some_file(filename)
    except IOError as err:
        print('Something went wrong reading {0}'.format(err))
    pass

def test_some_file_differently():
    filename = 'c:\\temp\\a.txt'
    try:
        read_some_file_differently(filename)
    except IOError as e:
        print('Something went wrong reading {0}: {1}'.format(filename, e))
    finally:
        print('Done.')
    return

if __name__ == '__main__':
    print("Hi!")
    #test_some_file()
    test_some_file_differently()