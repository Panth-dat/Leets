class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            n=nums[i]
            sum = 0
            while n > 0:
                sum += n % 10
                n //= 10
            if sum==i:
                return i   
        return -1