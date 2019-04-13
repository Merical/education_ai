# def threeSum(self, nums: List[int]) -> List[List[int]]:
#     if len(nums) < 3:
#         return []
#     ans = []
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             for k in range(j + 1, len(nums)):
#                 if nums[i] + nums[j] + nums[k] == 0:
#                     temp = self.quicksort([nums[i], nums[j], nums[k]])
#                     if temp not in ans:
#                         ans.append(temp)
#
#     return ans


# def quicksort(array):
#     if len(array) < 2:
#         return array
#     else:
#         pivot = array[0]
#         less = [i for i in array[1:] if i <= pivot]
#         greater = [i for i in array[1:] if i > pivot]
#         return quicksort(less) + [pivot] + quicksort(greater)
#
# def threeSum(nums):
#     if len(nums) < 3:
#         return []
#     nums = quicksort(nums)
#     print(nums)
#     i, j = 0, len(nums) - 1
#     ans = []
#     count = 0
#     while i < j:
#         compare = 0 - nums[i] - nums[j]
#         if compare in nums[(i + 1):j]:
#             temp = [nums[i], nums[nums.index(compare)], nums[j]]
#             ans.append(temp) if temp not in ans else None
#         if count % 2 == 0:
#             i += 1
#         else:
#             j -= 1
#         count += 1
#
#     return ans


def threeSum(nums):
    if len(nums) < 3:
        return []
    nums.sort()
    ans = []
    l = 0
    while l < len(nums) - 2 and nums[l] <= 0:
        if l > 0 and nums[l] == nums[l - 1]:
            l += 1
            continue

        m, r = l + 1, len(nums) - 1
        while m < r:
            total = nums[l] + nums[m] + nums[r]
            if total > 0:
                r -= 1
            elif total < 0:
                m += 1
            else:
                temp = [nums[l], nums[m], nums[r]]
                ans.append(temp) if temp not in ans else None
                while m < r and nums[m] == nums[m + 1]:
                    m += 1
                while r > m and nums[r] == nums[r - 1]:
                    r -= 1
                m += 1
                r -= 1
        l += 1
    return ans


print(threeSum([-1,0,1,2,-1,-4]))