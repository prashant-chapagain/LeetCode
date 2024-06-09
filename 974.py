class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        total = 0
        rem = {0:1}
        for i,n in enumerate(nums):
            total+=n
            r = total % k
            if(r<0):
                r+=k
            if(r  in rem):
                count += rem[r]
                rem[r] +=1
            else :
                rem[r] = 1
        return count
        