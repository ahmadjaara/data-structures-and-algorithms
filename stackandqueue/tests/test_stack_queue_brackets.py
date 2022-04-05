from stackandqueue.stack_queue_brackets import validate_bracket


def test_balance_same_bracket():
    string="{{}}[]{}()"
    actual=validate_bracket(string)
    expected=True
    assert expected==actual


def test_balance_not_same_bracket():
    string="{{)}{]{}()"
    actual=validate_bracket(string)
    expected=False
    assert expected==actual

def test_balance_same_bracket_with_words():
    string="{{helloworld}}[]{}()hjgjf"
    actual=validate_bracket(string)
    expected=True
    assert expected==actual

def test_open_bracket_only():
    string="{{([{(["
    actual=validate_bracket(string)
    expected=False
    assert expected==actual
    

