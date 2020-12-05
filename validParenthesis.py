from collections import deque


def isValid(s):
    mapping = {'(': ')', '{': '}', '[': ']'}
    stack = deque()

    for c in s:
        if c in mapping.keys():
            stack.append(c)
        elif not stack:
            return False
        else:
            top = stack.pop()
            if c == mapping[top]:
                continue
            else:
                return False
    return not stack


s = '{}{}()'
print(isValid(s))
