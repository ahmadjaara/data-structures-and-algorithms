from merge_sort.merge_sort import Merge,Mergesort

def test_merge_sort1():
    array =[15,100,-1,0,6]
    assert Mergesort(array)==[-1,0,6,15,100]


def test_merge_sort2():
    array =[15,100,-1,0,6,-12]
    assert Mergesort(array)==[-12,-1,0,6,15,100]