class Solution:
    def searchRange(self, nums, target: int):
        if len(nums) == 0:
            return [-1, -1]

        low = 0
        high = len(nums)
        while low < high:
            mid = (low + high) // 2
            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid

        left = low
        if left == len(nums) or nums[left] != target:
            return [-1, -1]

        low = 0
        high = len(nums)
        while low < high:
            mid = (low + high) // 2
            if target < nums[mid]:
                high = mid
            else:
                low = mid + 1
        right = low - 1
        return [left, right]





solution = Solution()
print(solution.searchRange([2, 2], target=2))

