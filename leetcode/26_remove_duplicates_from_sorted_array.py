class Solution:
    def removeDuplicates(self, nums):
        memo = {}
        for i in nums:
            if i in memo.keys():
                memo[i] += 1
            else:
                memo[i] = 0
        ans: int = len(memo.values())
        repeat = list(memo.values())
        for i in range(len(repeat)):
            for j in range(repeat[i]):
                del nums[i]
        return ans

    def removeDuplicatesTwoPointer(self, nums):
        if len(nums) == 0: return 0
        else:
            i: int = 0
            for j in range(1, len(nums)):
                if nums[j] != nums[i]:
                    i += 1
                    nums[i] = nums[j]
            return i + 1

solution = Solution()
# print(solution.removeDuplicates([1,1,1,1]))
print(solution.removeDuplicatesTwoPointer([1,2,3,4]))
