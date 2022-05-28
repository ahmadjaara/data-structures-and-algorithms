from quick_sort.code import *

def test_case1():
    reversesorted=[20,18,12,8,5,-2]
    quickSort(reversesorted,0,len(reversesorted)-1)

    assert reversesorted == [-2,5,8,12,18,20]

def test_case2():
    fewuniques=[5,12,7,5,5,7]
    quickSort(fewuniques,0,len(fewuniques)-1)

    assert fewuniques == [5, 5, 5, 7, 7, 12]
   
def test_case3():
    nearlysorted = [2,3,5,7,13,11]
    quickSort(nearlysorted,0,len(nearlysorted)-1)

    assert nearlysorted == [2,3,5,7,11,13]
