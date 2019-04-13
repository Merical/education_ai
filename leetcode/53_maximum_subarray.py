'''
def maxSubArray(nums) -> int:
    minimum = 0
    summary = 0
    output = nums[0]

    for i in nums:
        summary += i
        if summary - minimum > output:
            output = summary - minimum
        if summary < minimum:
            minimum = summary

    return output
'''
def dac(nums):
    n = len(nums)
    if n == 1: return nums[0], nums[0], nums[0], nums[0]
    out1 = dac(nums[:n//2])
    out2 = dac(nums[n//2:])
    l = max(out1[0], out1[3]+out2[0])
    m = max(out1[2]+out2[0], max(out1[1], out2[1]))
    r = max(out1[2]+out2[3], out2[2])
    s = out1[3] + out2[3]
    return l, m, r, s

def maxSubArray(nums):
    output = dac(nums)
    return output[1]


print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))