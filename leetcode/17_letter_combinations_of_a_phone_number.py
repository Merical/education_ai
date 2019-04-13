def letterCombinations(digits: str):
    phone = {'2': 'abc',
             '3': 'def',
             '4': 'ghi',
             '5': 'jkl',
             '6': 'mno',
             '7': 'pqrs',
             '8': 'tuv',
             '9': 'wxyz'}
    memo = []
    if len(digits) == 0:
        return []
    else:
        for i in digits:
            memo.append(phone[i])

        return getCombinations(memo)


def getCombinations(strings):
    if len(strings) == 1:
        return [i for i in strings[0]]
    else:
        mid = len(strings) // 2
        left = getCombinations(strings[:mid])
        right = getCombinations(strings[mid:])
        output = []
        for l in left:
            for j in right:
                output.append(l+j)
        return output

print(letterCombinations('23'))