class Solution:
    def removeElement(self, nums, val: int) -> int:
        if len(nums) == 0: return 0
        else:
            i: int = 0
            for j in range(len(nums)):
                if nums[j] != val:
                    nums[i] = nums[j]
                    i += 1
            return i

solution = Solution()
print(solution.removeElement([3, 2, 2, 3], 3))