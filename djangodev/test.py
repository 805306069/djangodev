"""
最大连续数列
给定一个整数数组，找出总和最大的连续数列，并返回总和。
示例：
输入： [-2,1,-3,4,-1,2,1,-5,4]
输出： 6
解释： 连续子数组 [4,-1,2,1] 的和最大，为 6。

"""

def max_num(nums):
    n = len(nums)
    if n == 0:
        return nums
    dps = [0]*n
    dps[0] = nums[0]
    for i in range(1,n):
        dps[i] = max(dps[i-1] + nums[i], nums[i])
    return max(dps)

#1.题目输入[-2,1,-3,4,-1,2,1,-5,4]
nums = [-2,1,-3,4,-1,2,1,-5,4]
#2.【】
#3.【0】
#4.【-1】

print(max_num(nums))
