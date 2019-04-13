import time

# def maxArea(height):
#         if len(height) <= 1:
#             return 0
#         water = {}
#
#         tic = time.time()
#         for i, h_1 in enumerate(height):
#             for j, h_2 in enumerate(height[i+1:]):
#                 if (i, j) not in water:
#                     water[i, j] = abs(j + 1) * min(h_1, h_2)
#         print('LCH: the time cost is ', time.time() - tic, ' seconds.')
#
#         tic = time.time()
#         ans = max(water.values())
#         print('LCH: the time cost is ', time.time() - tic, ' seconds.')
#         return ans

def maxArea(height):
    if len(height) <= 1:
        return 0
    i = 0
    j = len(height) - 1
    maximum = 0

    while i < j:
        temp = (j - i) * min(height[i], height[j])
        if temp > maximum:
            maximum = temp

        if height[i] > height[j]:
            j -= 1
        else:
            i += 1

    return maximum



input = [1,8,6,2,5,4,8,3,7]
output = maxArea(input)
print(output)