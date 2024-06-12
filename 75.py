class Solution:
    def sortColors(self, nums):
        count = [0] * 3
        for num in nums:
            count[num] += 1
        
        i = 0
        for color, freq in enumerate(count):
            for _ in range(freq):
                nums[i] = color
                i += 1
        