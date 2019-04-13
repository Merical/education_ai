def threeSumClosest(nums, target) -> int:
    nums.sort()
    length = len(nums)
    memo = {}
    if length  == 0:
        return 0
    elif length == 1:
        return nums[0]
    elif length == 2:
        return nums[0] + nums[1]
    else:
        closest = nums[0] + nums[1] + nums[2]
        for l in range(length-2):
            m = l + 1
            r = length-1

            while m < r:
                if not (l, m, r) in memo:
                    memo[l, m, r] = nums[l] + nums[m] + nums[r]

                if abs(closest - target) >= abs(memo[l, m, r] - target):
                    closest = memo[l, m, r]

                if memo[l, m, r] > target:
                    r -= 1
                elif memo[l, m, r] < target:
                    m += 1
                else:
                    return target
        return closest

print(threeSumClosest([-3,-2,-5,3,-4], -1))