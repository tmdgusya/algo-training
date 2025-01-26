from typing import List

def pop(list: List, default):
    try:
        return list.pop()
    except:
        return default

"""
5555 + 55 = 5610
5 5 1 0000
5 5 1 0010
5 0 0 0610
5 0 0 5610
5610 5610 OK
"""
def add(str1: str, str2: str):
    """
    carry = 1

    x = str1.pop(default=0)
    y = str2.pop(default=0)
    result = x + y + carry
    """
    carry = 0
    list1 = list(str1)
    list2 = list(str2)
    previous = ""

    for idx in range(max(len(list1), len(list2))):
        x = pop(list1, 0)
        y = pop(list2, 0)
        carry = 0
        add_result = str(int(x) + int(y) + int(carry))

        if len(add_result) == 2:
            carry = add_result[0]
            r = add_result[1]
        else:
            carry = 0
            r = add_result[0]

        print(f"{x} {y} {carry} {previous}")
        previous = r + previous
    
    if carry != 0:
        previous = carry + previous
    
    return previous

print(add("9", "10"))
    