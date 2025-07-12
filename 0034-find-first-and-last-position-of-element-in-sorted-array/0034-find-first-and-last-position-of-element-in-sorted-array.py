class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        f=-1
        l=-1
        for i in range(len(nums)):
            if nums[i]==target and f==-1:
                f=i
            if nums[i]==target:
                l=i
        return[f,l]