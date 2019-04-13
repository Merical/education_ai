def longestPalindrome(s: str) -> str:
    end = 0
    start = 0

    if len(s) == 0:
        return ''
    elif len(s) == 1:
        return s
    else:
        for i in range(0, len(s)):
            len1 = expandAroundCenter(s, i, i)
            len2 = expandAroundCenter(s, i, i + 1)
            lenth = max(len1, len2)
            if lenth > end - start:
                start = i
                end = i + lenth // 2
    return s[start:end + 1]


def expandAroundCenter(s, L, R):
    while (L >= 0 and R < len(s) and s[L] == s[R]):
        L -= 1
        R += 1
    return R - L - 1

print(longestPalindrome('bb'))