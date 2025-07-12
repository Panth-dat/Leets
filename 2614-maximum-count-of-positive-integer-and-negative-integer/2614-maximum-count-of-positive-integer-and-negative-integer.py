class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        neg=bisect.bisect_left(nums,0)
        pos=len(nums)-bisect.bisect_right(nums,0)
        return max(neg,pos)