# def longestCommonPrefix(strs) -> str:
#         if len(strs) == 0:
#             return ""
#         elif len(strs) == 1:
#             return strs[0]
#         else:
#             lengths = []
#             output = ''
#             for i in strs:
#                 lengths.append(len(i))
#             index = lengths.index(min(lengths))
#             min_length = min(lengths)
#             shortest = strs[index]
#             for i in range(min_length):
#                 flag = True
#                 for s in strs:
#                     if s[i] == shortest[i]:
#                         continue
#                     else:
#                         flag = False
#                         break
#                 if flag:
#                     output += shortest[i]
#                 else:
#                     break
#             return output

def longestCommonPrefix(strs) -> str:
    print('the function applied')
    length = len(strs)
    if length == 0:
        return ''
    elif length == 1:
        return strs[0]
    else:
        mid = length // 2
        leftpart = longestCommonPrefix(strs[:mid])
        rightpart =longestCommonPrefix(strs[mid:])
        i = 0
        while i < min(len(leftpart), len(rightpart)):
            if leftpart[i] != rightpart[i]:
                return leftpart[:i]
            i += 1
        return leftpart[:i]

print(longestCommonPrefix())