import pytest
from linklist.linklist import Linklist
from linklist.linklist import Node

def test_linklist_empty():
    """
    test to check if the linklist class
    Can successfully instantiate an empty linked list
    """
    ll = Linklist()
    expected = None
    actual = ll.head
    assert expected == actual

# @pytest.mark.skip("pending")
def test_insert():
    """
    test to check if the linklist class
    Can properly insert node at the begining of the linked list
    """
    ll=Linklist()
    ll.insert_begining("l")
    expected="l"
    actual=ll.head.data
    assert expected == actual
def test_head_pointer():
    """
    test to check if the head of linklist class
    can properly point to
    the first node in the linked list

    """
    ll=Linklist()
    ll.insert_begining('1')
    expected =None
    actual=ll.head.next
    assert expected == actual
# @pytest.mark.skip("pending")
def test_insert_multiple_node():
    """
    test to check if the linklist class
    Can properly insert multiple node at the begining of the linked list

    """
    ll=Linklist()
    ll.insert_begining("1")
    ll.insert_begining("2")
    ll.insert_begining("3")
    ll.insert_begining("4")
    
    expected ="4 -->3 -->2 -->1 -->None"
    
    actual =ll.display()
    
    assert expected == actual

def test_search_ele_exist():
    """
    test to check if the linklist class
    can return true when finding a value within the linked list that exists
    using search method

    """
    ll=Linklist()
    ll.insert_begining("1")
    ll.insert_begining("2")
    ll.insert_begining("3")
    ll.insert_begining("4")
    
    expected =True
    
    actual =ll.search_ele("3")
    
    assert expected == actual

def test_search_ele_not_exist():
    """
    test to check if the linklist class
    can return false when searching for a value in the linked list that does not exist
    using search method

    """
    ll=Linklist()
    ll.insert_begining("1")
    ll.insert_begining("2")
    ll.insert_begining("3")
    ll.insert_begining("4")
    
    expected =False
    
    actual =ll.search_ele("10")
    
    assert expected == actual

def test_return_all_collecation_in_linklist():
    """
    test to check if the linklist class
    Can properly return a collection of all the values that exist in the linked list

    """   
    ll=Linklist()
    ll.insert_begining("1")
    ll.insert_begining("2")
    ll.insert_begining("3")
    ll.insert_begining("4")
    
    expected ="4 -->3 -->2 -->1 -->None"
    
    actual =ll.display()
    
    assert expected == actual