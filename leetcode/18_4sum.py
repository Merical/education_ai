def fourSum(nums, target):
    if len(nums) < 4:
        return []
    nums.sort()
    print(nums)
    length = len(nums)
    ans = []
    l = 0
    while l < length-3 and nums[l] <= target//4:

        m_l = l + 1
        while m_l < length-2:
            m_r = m_l + 1
            r = length - 1
            while m_r < r:
                total = nums[l] + nums[m_l] + nums[m_r] + nums[r]
                if total > target:
                    r -= 1
                elif total < target:
                    m_r += 1
                else:
                    temp = [nums[l], nums[m_l], nums[m_r], nums[r]]
                    ans.append(temp) if temp not in ans else None
                    r -= 1
                    m_r += 1

            m_l +=1

        l += 1

    return ans

print(fourSum([0,4,-5,2,-2,4,2,-1,4], 12))