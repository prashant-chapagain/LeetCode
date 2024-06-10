class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        Count = 0
        sortedHeight = sorted(heights) 
        for i in range(len(heights)):
            if heights[i] != sortedHeight[i]:
                Count += 1
        return Count
        