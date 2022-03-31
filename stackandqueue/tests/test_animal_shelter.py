from stackandqueue.AnimalShelter import AnimalShelter

def test_deque_on_empty_queue_dog():
  empty_queue= AnimalShelter()

  actual = empty_queue.dequeue_pets("dog")
  expected = "queue is empty"
  assert actual == expected

def test_deque_on_empty_queue_cat():
  empty_queue= AnimalShelter()

  actual = empty_queue.dequeue_pets("cat")
  expected = "queue is empty"
  assert actual == expected

def test_enque_on_empty_queue_dog():
  empty_queue_dog= AnimalShelter()
  
  empty_queue_dog.enqueue("cat")
  empty_queue_dog.enqueue("dog")
  empty_queue_dog.enqueue("dog")
  
  actual = empty_queue_dog.dequeue_pets("dog")
  expected = "dog"
  assert actual == expected

def test_enque_on_empty_queue_cat():
  empty_queue_cat= AnimalShelter()
  
  empty_queue_cat.enqueue("cat")
  empty_queue_cat.enqueue("dog")
  empty_queue_cat.enqueue("dog")
  
  actual = empty_queue_cat.dequeue_pets("cat")
  expected = "cat"
  assert actual == expected

def test_enque_on_not_cat_dog_animal():
  empty_queue_cat= AnimalShelter()
  
  actual =  empty_queue_cat.enqueue("ant")
  expected = 'not dog or cat'
  assert actual == expected

