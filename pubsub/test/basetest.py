'''
Created on Apr 23, 2014

@author: vsa
'''
import unittest
from pubsub.base import Event
from pubsub.base import ID
from pubsub.base import Publisher
from pubsub.base import Subscriber
from pubsub.base import Dispatcher

class DispatcherTester(Dispatcher):
    def check_publisher_registered(self, p):
        return p in self.publisher_subscriber_map
    
    def check_subscriber_registered(self, p, s):
        if not self.check_publisher_registered(p):
            return False
        
        subscribers = self.publisher_subscriber_map[p]
        if subscribers is None:
            return False
        elif s not in subscribers:
            return False
        else:
            return True

class SubscriberTester(Subscriber):
    def __init__(self):
        Subscriber.__init__(self)
        self.received_events = []
    
    def deliver(self, pid, e):
        super(SubscriberTester, self).deliver(pid, e)
        self.received_events.append(e)
        
class Test(unittest.TestCase):

    def testID(self):
        id1 = ID()
        id2 = ID()
        assert id1 != id2
        
        s = set()
        s.add(id1)
        s.add(id2)
        assert len(s) == 2
        assert id1 in s
        assert id2 in s

    def testEvent(self):
        e1 = Event()
        assert e1 == e1.id
        
        e2 = Event()
        assert e1 != e2

    def testPublisher(self):
        p1 = Publisher()
        p2 = Publisher()
        assert p1 != p2
        
        s = set()
        s.add(p1)
        s.add(p2)
        assert len(s) == 2
        assert p1 in s
        assert p1.id in s
        assert p2 in s
        assert p2.id in s
        
    def testSubscriber(self):
        s1 = Subscriber()
        s2 = Subscriber()
        assert s1 != s2
        
        s = set()
        s.add(s1)
        s.add(s2)
        assert len(s) == 2
        assert s1 in s
        assert s1.id in s
        assert s2 in s
        assert s2.id in s
        
    def testDispatcher(self):
        d = DispatcherTester()
        
        try:
            d.register_subscriber(None, None)
        except Exception:
            pass
        else:
            assert False

        try:
            d.register_publisher(None)
        except Exception:
            pass
        else:
            assert False
        
        s1 = SubscriberTester()
        p1 = Publisher()
        try:
            d.register_subscriber(p1, None)
        except Exception:
            pass
        else:
            assert False
        
        d.register_publisher(p1)
        d.check_publisher_registered(p1)
        d.register_subscriber(p1, s1)
        d.check_subscriber_registered(p1, s1)
        
        s2 = SubscriberTester()
        d.register_subscriber(p1, s2)
        d.check_subscriber_registered(p1, s2)
        
        e1 = Event()
        d.emit(p1, e1)
        if e1 not in s1.received_events:
            raise Exception('Event {0} not received by subscriber {1}.'.format(e1, s1))
        if e1 not in s2.received_events:
            raise Exception('Event {0} not received by subscriber {1}.'.format(e1, s2))
        
        e2 = Event()
        p2 = Publisher()
        d.emit(p2, e1)
        if e2 in s1.received_events:
            raise Exception('Event {0} should not be received by subscriber {1}.'.format(e2, s1))
        if e2 in s2.received_events:
            raise Exception('Event {0} should not be received by subscriber {1}.'.format(e2, s2))
        
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
