def romanToInt(s: str) -> int:
    Symbol = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    s = s[::-1]
    output = Symbol[s[0]]
    criterion = s[0]
    for i in range(1, len(s)):
        if Symbol[s[i]] >= Symbol[criterion]:
            output = output + Symbol[s[i]]
            criterion = s[i]
        else:
            output = output - Symbol[s[i]]

    return output

print(romanToInt('IV'))