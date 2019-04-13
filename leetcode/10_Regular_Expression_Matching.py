#
# def isMatch(s: str, p: str) -> bool:
#         pattern = p
#         text = s
#
#         if not pattern:
#             return not text
#
#         first_match = bool(text) and pattern[0] in {text[0], '.'}
#         if len(pattern) >= 2 and pattern[1] == '*':
#             return (isMatch(text, pattern[2:]) or first_match and isMatch(text[1:], pattern))
#         else:
#             return first_match and isMatch(text[1:], pattern[1:])


def isMatch(s: ptr, p: str) -> bool:
        text = s
        pattern = p

        def dp(i, j):
            if j == len(pattern):
                ans = i == len(text)
            else:
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    ans = dp(i, j+2) or first_match and dp(i+1, j)
                else:
                    ans = first_match and dp(i+1, j+1)

            return ans

        return dp(0, 0)