def _removeInvalidParentheses(string, min_remove,ans, visited):
    if string in visited: return
    visited.add(string)
    if min_remove == 0 and minimum_removal(string) == 0:
        ans.append(string)
        visited.add(string)
        return
    for idx in range(len(string)):
        if string[idx] not in {'(',')'}:
            continue
        # print(string[0:idx] + string[idx+1:])
        _removeInvalidParentheses(string[0:idx] + string[idx+1:], min_remove -1, ans, visited)



def removeInvalidParentheses(string):
    min_num = minimum_removal(string)
    print(string)
    ans = []
    visited = set()
    _removeInvalidParentheses(string, min_num, ans, visited)
    return (ans) if len(ans) != 0 else [""]

def minimum_removal(string):
    stack = []
    for char in string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0:
                stack.append(char)
            elif stack[-1] == ')':
                stack.append(char)
            elif stack[-1] == '(':
                stack.pop()

    return len(stack)

print(removeInvalidParentheses("()())()"))
