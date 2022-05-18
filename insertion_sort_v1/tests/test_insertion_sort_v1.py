from insertion_sort_v1.insertion_sort import insertionSort

def test_insetrionsort():
    arr=[5,1,-1,10,0]
    assert insertionSort(arr)==[-1,0,1,5,10]

def test_insetrionsort_2():
    arr=[100,5,1,-1,10,0]
    assert insertionSort(arr)==[-1,0,1,5,10,100]
