def reverse(x: int) -> int:
    flag = None
    if x == 0 or x > 2 ** 31 - 1 or x < -2 ** 31: return 0
    elif x < 0:
        x = -x
        flag = '-'
    s = str(x)[::-1]
    while s[0] == '0':
        s = s[1:]

    s = flag + s if flag is not None else s
    return int(s)

print(reverse(1534236469))