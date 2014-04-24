'''
Created on Apr 23, 2014

@author: vsa
'''

import uuid

class ID(object):
    '''
    ID is the unique identifier class for messages, subscribers and publisher
    '''
    
    def __init__(self):
        self._v = uuid.uuid4()
        
    def __repr__(self):
        return str(self._v)
    
    def __eq__(self, other):
        if other is None:
            return False
        elif isinstance(other, ID):
            return self._v == other._v
        elif isinstance(other, str):
            return str(self._v) == other
        else:
            return False
        
    def __hash__(self):
        return hash(self._v)
    
    def __lt__(self, other):
        if other is None:
            raise Exception('Cannot compare to None')
        elif isinstance(other, ID):
            return self._v < other._v
        elif isinstance(other, str):
            return str(self._v) < other
        else:
            return False


    def __gt__(self, other):
        if other is None:
            raise Exception('Cannot compare to None')
        elif isinstance(other, ID):
            return self._v > other._v
        elif isinstance(other, str):
            return str(self._v) > other
        else:
            return False

class Event(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.id = ID()
        
    def __eq__(self, other):
        if other is None:
            return False
        elif isinstance(other, ID):
            return self.id == other
        elif isinstance(other, str):
            return self.id == other
        elif isinstance(other, Event):
            return self.id == other.id
        else:
            return False

    def __hash__(self):
        return hash(self.id)
    
    def __repr__(self):
        return 'Event-{0}'.format(self.id)
    
                   
class Publisher(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.id = ID()
        
    def __eq__(self, other):
        if other is None:
            return False
        elif isinstance(other, ID):
            return self.id == other
        elif isinstance(other, str):
            return self.id == other
        elif isinstance(other, Publisher):
            return self.id == other.id
        else:
            return False
        
    def __lt__(self, other):
        if other is None:
            raise Exception('Cannot compare to None.')
        elif isinstance(other, ID):
            return self.id < other
        elif isinstance(other, str):
            return self.id < other
        elif isinstance(other, Publisher):
            return self.id < other.id
        else:
            raise Exception('Do not support comparison with type {0}.'.format(other.__class__))
    
    def __gt__(self, other):
        if other is None:
            raise Exception('Cannot compare to None.')
        elif isinstance(other, ID):
            return self.id > other
        elif isinstance(other, str):
            return self.id > other
        elif isinstance(other, Publisher):
            return self.id > other.id
        else:
            raise Exception('Do not support comparison with type {0}.'.format(other.__class__))

    def __hash__(self):
        return hash(self.id)
    
class Subscriber(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.id = ID()
    
    def __eq__(self, other):
        if other is None:
            return False
        elif isinstance(other, ID):
            return self.id == other
        elif isinstance(other, str):
            return self.id == other
        elif isinstance(other, Subscriber):
            return self.id == other.id
        else:
            return False
        
    def __lt__(self, other):
        if other is None:
            raise Exception('Cannot compare to None.')
        elif isinstance(other, ID):
            return self.id < other
        elif isinstance(other, str):
            return self.id < other
        elif isinstance(other, Subscriber):
            return self.id < other.id
        else:
            raise Exception('Do not support comparison with type {0}.'.format(other.__class__))
    
    def __gt__(self, other):
        if other is None:
            raise Exception('Cannot compare to None.')
        elif isinstance(other, ID):
            return self.id > other
        elif isinstance(other, str):
            return self.id > other
        elif isinstance(other, Subscriber):
            return self.id > other.id
        else:
            raise Exception('Do not support comparison with type {0}.'.format(other.__class__))

    def __hash__(self):
        return hash(self.id)
    
    def deliver(self, pid, e):
        if pid is None:
            raise Exception('Pid cannot be None.')
        if e is None:
            raise Exception('Event cannot be None.')
        if not isinstance(pid, ID):
            raise Exception('Expected {0}, received {1}.'.format(ID, pid.__class__))
        if not isinstance(e, Event):
            raise Exception('Expected {0}, received {1}.'.format(Event, e.__class__))
        if e is None:
            raise Exception('Cannot deliver None.')
        elif not isinstance(e, Event):
            raise Exception('Can only deliver an Event not a {0}.'.format(e.__class__))
          
class Dispatcher(object):
    '''
    Dispatcher
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.id = ID()
        self.publisher_subscriber_map = {}
        
    def register_publisher(self, p):
        if p is None:
            raise Exception('Argument is None.')
        elif not isinstance(p, Publisher):
            raise Exception('Argument must be of type {0} - it is {1}'.format(Publisher, p.__class__))
        
        self.publisher_subscriber_map[p] = set()
        
    def register_subscriber(self, p, s):
        if isinstance(p, ID):
            pid = p
        elif isinstance(p, Publisher):
            pid = p.id
        
        if pid is None:
            raise Exception('P/Pid cannot be None.')
        
        if pid not in self.publisher_subscriber_map:
            raise Exception('Publisher {0} is not registered.'.format(pid))

        sub_set = self.publisher_subscriber_map[pid]
        sub_set.add(s)
    
    def emit(self, p, e):
        if p is None:
            raise Exception('P/Pid cannot be None.')
        if e is None:
            raise Exception('Event cannot be None.')
        if isinstance(p, Publisher):
            pid = p.id
        else:
            pid = p
        
        if pid not in self.publisher_subscriber_map:
            return False
        
        subscriber_set = self.publisher_subscriber_map[pid]
        for s in subscriber_set:
            s.deliver(pid, e)
            
        return True

