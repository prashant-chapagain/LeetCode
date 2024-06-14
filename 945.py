class Solution(object):
    def minIncrementForUnique(self, nums):
        nums.sort()
        op = 0
        for i in range(1,len(nums)):
            if nums[i] <= nums[i-1]:
                increment = nums[i-1] + 1 - nums[i]
                nums[i] = nums[i-1]+1
                op += increment
        return op
