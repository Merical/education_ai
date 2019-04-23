class Solution:
    def generateParenthesis(self, n: int):
        '''
        the backtrack do "((()))" -> "(()())" -> "(())()" -> "()(())" -> "()()()"

        :param n:
        :return:
        '''
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append(S)
                return
            if left < n:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans

    def generateParenthesisClosure(self, n: int):
        '''
        see the ( at the begin and ) at the end

        :param n:
        :return:
        '''
        if n == 0: return ['']
        ans = []
        for c in range(n):
            for left in self.generateParenthesisClosure(c):
                for right in self.generateParenthesisClosure(n-c-1):
                    ans.append('({}){}'.format(left, right))
        return ans


solution = Solution()
# print(solution.generateParenthesis(3))
print(solution.generateParenthesisClosure(3))
