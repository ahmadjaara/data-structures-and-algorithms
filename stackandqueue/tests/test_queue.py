from stackandqueue.queue import Queue,Node
import pytest

def test_init_empty_stack():
  empty_queue= Queue()

  actual = empty_queue.front
  expected = None
  assert actual == expected

def test_deque_on_empty_queue():
  empty_queue=Queue()
  actual= empty_queue.dequeue()
  expected ="queue is empty"
  assert actual == expected

def test_peek_on_empty_queue():
  empty_queue=Queue()
  actual= empty_queue.peek()
  expected ="queue is empty"
  assert actual == expected

def test_enqueue(queue):

  actual = queue.front.value
  expected = 5
  assert actual == expected

def test_enqueue_multi(queue):

  queue.enqueue(1)
  queue.enqueue(0)

  actual = queue.front.value
  expected = 5
  assert actual == expected
  
def test_dequeue(queue):
 
  actual= queue.dequeue()
  expected =5
  assert actual == expected

def test_dequeue_multi(queue):
  queue.dequeue()
  queue.dequeue()
  queue.dequeue()

  actual= queue.dequeue()
  expected ="queue is empty"
  assert actual == expected


def test_peek_of_queue(queue):
  
  actual = queue.peek()
  expected = 5
  assert actual == expected


def test_is_empty_queue():
  
  queue_epmty=Queue()
  actual = queue_epmty.is_empty()
  expected = True
  assert actual == expected
  

 #decorator
@pytest.fixture
def queue():

    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(3)
    queue.enqueue(2)

    return queue