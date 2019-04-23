class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        else:
            database = []
            for i in range(len(haystack)-len(needle)+1):
                database.append(haystack[i:i+len(needle)])
            if needle in database:
                return database.index(needle)
            else:
                return -1

solution = Solution()
print(solution.strStr("hello", "ll"))