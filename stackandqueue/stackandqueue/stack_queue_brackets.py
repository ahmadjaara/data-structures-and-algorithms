from stackandqueue.stack import Stack


def validate_bracket(string):
    """
    function representing whether or not the brackets in the string are balanced
    Return: boolean
    if it balance Return True
    if not balance Return False 
    input : string 
    output:string 
    """
    bracket=Stack()
    for i in string:

        if i in ["(", "{", "["]:
           bracket.push(i)

        elif i in [")", "}", "]"]:

            if bracket.is_empty():
                return False
            current_bracket = bracket.pop()
            if current_bracket == '(':
                if i != ")":
                    return False
            if current_bracket == '{':
                if i != "}":
                    return False
            if current_bracket == '[':
                if i != "]":
                    return False
        else:
            continue

          
    # Check Empty Stack
    if not bracket.is_empty():
        return False
    return True
if __name__=="__main__":
    print(validate_bracket("[]{}") )