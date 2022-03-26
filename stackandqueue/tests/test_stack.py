from stackandqueue.stack import Stack,Node
import pytest


def test_init_empty_stack():
  empty_stack= Stack()

  actual = empty_stack.top
  expected = None
  assert actual == expected

def test_pop_on_empty_stack():
  empty_stack=Stack()
  actual= empty_stack.pop()
  expected ="empty stack"
  assert actual == expected

def test_peek_on_empty_stack():
  empty_stack=Stack()
  actual= empty_stack.peek()
  expected ="empty stack"
  assert actual == expected

def test_push(stack):

  actual = stack.top.value
  expected = 2
  assert actual == expected

def test_push_multi(stack):

  stack.push(1)
  stack.push(0)

  actual = stack.top.value
  expected = 0
  assert actual == expected
  
def test_pop(stack):
  
  actual= stack.pop()
  expected =2
  assert actual == expected

def test_pop_multi(stack):
  stack.pop()
  stack.pop()
  stack.pop()

  actual= stack.pop()
  expected ="empty stack"
  assert actual == expected


def test_peek_of_stack(stack):
  

  actual = stack.peek()
  expected = 2
  assert actual == expected


def test_is_empty_stack():
  stack=Stack()
  actual = stack.is_empty()
  expected = True
  assert actual == expected



 #decorator
@pytest.fixture
def stack():
 
  stack = Stack()
  stack.push(5)
  stack.push(3)
  stack.push(2)

  return stack

  
