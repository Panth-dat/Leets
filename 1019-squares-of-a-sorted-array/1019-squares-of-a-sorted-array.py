class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x=[]
        for i in nums:
            x.append(i**2)
        x.sort()
        return x