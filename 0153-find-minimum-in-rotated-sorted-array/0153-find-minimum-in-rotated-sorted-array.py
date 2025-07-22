class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        b=0
        e=len(nums)-1
        while b<=e:
            m=(b+e)//2
            if b==e:
                return nums[b]
            if nums[m] >= nums[b] and nums[b]>nums[e]:
                b=m+1
            else:
                e=m
        return -1