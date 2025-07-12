class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        loc=-1
        b=0
        e=len(nums)-1
        while b<=e:
            mid=int((b+e)/2)
            if nums[mid]==target:
                return mid
            elif target<nums[mid]:
                e=mid-1
            else:
                b=mid+1
        return b
        