class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxans = 0
        dp = [0 for _ in range(len(s))]
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = dp[i-2] + 2 if i >= 2 else 2
                elif i - dp[i-1] > 0 and s[i - dp[i-1] - 1] == '(':
                    # dp[i] = dp[i - 1] + 2
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i-1] - 2] if i - dp[i-1] >= 2 else dp[i - 1] + 2
            maxans = max(maxans, dp[i])

        return maxans

    def longestValidParenthesesStack(self, s: str) -> int:
        if len(s) == 0: return 0
        maxans: int = 0
        stack: list = []
        stack.append(-1)
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    maxans = max(maxans, i - stack[-1])
        return maxans


solution = Solution()
# print(solution.longestValidParentheses('()(())'))
print(solution.longestValidParenthesesStack('))()(())'))
