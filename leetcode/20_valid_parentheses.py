class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        stack = []
        mapping = {'(':')', '{':'}', '[':']'}
        for i in s:
            if i in ['(', '{', '[']:
                stack.append(mapping[i])
            else:
                compare = stack.pop() if stack else '#'
                if compare != i:
                    return False
                else:
                    continue

        return not stack

solution = Solution()
print(solution.isValid("()[]{}"))