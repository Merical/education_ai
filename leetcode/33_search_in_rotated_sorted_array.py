class Solution:
    def search(self, nums, target: int) -> int:
        if len(nums) == 0:
            return -1
        else:
            l, r = 0, len(nums)-1
            while l <= r:
                mid = (l + r) >> 1
                if nums[mid] == target:
                    return mid
                if nums[l] <= nums[mid]:
                    if nums[l] <= target and target < nums[mid]:
                        r = mid - 1
                    else:
                        l = mid + 1
                else:
                    if nums[mid] < target and target <= nums[r]:
                        l = mid + 1
                    else:
                        r = mid - 1
            return -1

solution = Solution()
print(solution.search([4,5,6,7,0,1,2], target=0))
# print(solution.search([1, 3, 5], target=2))

