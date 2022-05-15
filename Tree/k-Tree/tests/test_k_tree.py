from k_tree.fiz_buz_fun import * 
# Tree/k-Tree/tests/test_k_tree.py

def test_k_tree():
    root = build_k_tree()
    assert root.data == 1
    assert root.children[0].data == 8
    assert root.children[1].data == 9

def test_fizzbuzz_tree():
    root = build_k_tree()
    fizz_buzz_tree(root)
    assert root.data == "1"
    assert root.children[0].data == "8"
    assert root.children[1].data == "Fizz"
    assert root.children[2].data == "4"
    assert root.children[1].children[1].data == "Fizz"
    assert root.children[2].children[1].data == "FizzBuzz"