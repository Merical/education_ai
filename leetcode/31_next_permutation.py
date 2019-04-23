class Solution:
    def nextPermutation(self, nums) -> list:
        if len(nums) < 2:
            return nums
        else:
            i = len(nums) - 2
            while i >= 0 and nums[i+1] <= nums[i]:
                i -= 1
            if i >= 0:
                j = len(nums) - 1
                while j >= 0 and nums[j] <= nums[i]:
                    j -= 1
                nums[i], nums[j] = nums[j], nums[i]
            l = i + 1
            r = len(nums) - 1
            while (l < r):
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            return nums


solution = Solution()
print(solution.nextPermutation([1, 2, 3]))
