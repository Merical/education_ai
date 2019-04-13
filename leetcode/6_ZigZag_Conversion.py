# def convert(s: str, numRows: int) -> str:
#         i = 0
#         output = ''
#         position = [0 for i in s]
#         while i < len(s):
#             count = 0
#             while count < numRows and i < len(s):
#                 position[i] = count
#                 count += 1
#                 i += 1
#
#             count = numRows - 2
#             while count > 0 and i < len(s):
#                 position[i] = count
#                 count -= 1
#                 i += 1
#
#         for row in range(numRows):
#             for i in range(len(s)):
#                 if position[i] == row:
#                     output += s[i]
#
#         return output

def convert(s: str, numRows: int) -> str:
    if numRows == 1: return s

    ret: str = ''
    cycleLen: int = 2 * numRows -2

    for i in range(numRows):
        j = 0
        while i + j < len(s):
            ret += s[i + j]
            if ((i != 0) and (i != numRows - 1) and (j + cycleLen - i < len(s))):
                ret += s[j + cycleLen - i]
            j += cycleLen

    return ret

print(convert("PAYPALISHIRING", 3))
