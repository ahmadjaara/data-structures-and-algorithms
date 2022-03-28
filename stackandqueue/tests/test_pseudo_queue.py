from stackandqueue.pseudo_queue import PseudoQueue
import pytest

def test_enqueue1():
    """adding elements using enqueue"""
    queue = PseudoQueue()
    queue.enqueue(6)
    queue.enqueue(1)
    queue.enqueue(9)

    actual=queue.dequeue()
    expected=6
    assert actual==expected


def test_enqueue2(queue):
    """adding elements using enqueue"""
    queue.enqueue(6)
    actual=queue.dequeue()
    expected=5
    assert actual==expected

def test_dequeue1(queue):
    """delete elements using dequeue"""
    queue.dequeue()
    queue.dequeue()
    actual=queue.dequeue()
    expected=2
    assert actual==expected

def test_dequeue2(queue):
    """delete elements using dequeue"""
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    actual=queue.dequeue()
    expected="queue is empty"
    assert actual==expected
    

#decorator
@pytest.fixture
def queue():

    queue = PseudoQueue()
    queue.enqueue(5)
    queue.enqueue(3)
    queue.enqueue(2)

    return queue