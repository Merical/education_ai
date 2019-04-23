import sys

# def my_ascii(n):
#     if 48 <= ord('n') <=57:
#         return ord('n')
#     else:
#         return ord(n) * 2 if n.islower() else ord(n.lower())*2 - 1
#
# def quicksort(names, compare=0):
#     if len(names) < 2:
#         return names
#     else:
#         pivot = names[0]
#         less = [i for i in names if my_ascii(i[compare]) < my_ascii(pivot[compare])]
#         greater = [i for i in names if my_ascii(i[compare]) > my_ascii(pivot[compare])]
#         mid = [i for i in names if my_ascii(i[compare]) == my_ascii(pivot[compare])]
#         return quicksort(less) + quicksort(mid, compare=compare+1) + quicksort(greater)

def quicksort(names, compare=0):
    if len(names) < 2:
        return names
    else:
        pivot = names[0]
        less = [i for i in names if (i[compare]) < (pivot[compare])]
        greater = [i for i in names if (i[compare]) > (pivot[compare])]
        mid = [i for i in names if (i[compare]) == (pivot[compare])]
        return quicksort(less) + quicksort(mid, compare=compare + 1) + quicksort(greater)

n = int(input())
if n > 1000:
    raise ValueError
names = []
repeat = 0
for i in range(n):
    name = input()
    if len(name) > 20:
        raise ValueError
    if name in names:
        repeat += 1
        count = 0
        for n in names:
            if n == name:
                count += 1
        name += str(count)

    names.append(name)

if repeat < len(names)-1:
    for i in range(len(names)):
        if len(names[i]) < 20:
            names[i] += '0' * (20 - len(names[i]))

    names = quicksort(names)
    for n in names:
        for i in range(10):
            n = n.replace(str(i), '')
        sys.stdout.write(n + '\n')
else:
    for n in names:
        for i in range(10):
            n = n.replace(str(i), '')
        sys.stdout.write(n + '\n')
