class Solution:

    def isValid(self, s):
        open_brackets = ('(', '{', '[')
        valid = (('(', ')'), ('{', '}'), ('[', ']'))
        stack = []
        for i in s:
            try:
                if i in open_brackets:
                    stack.append(i)
                elif (stack.pop(), i) in valid:
                    continue
                else:
                    return False
            except IndexError:
                return False
        return False if len(stack) != 0 else True


s = Solution()
print(s.isValid(']'))
