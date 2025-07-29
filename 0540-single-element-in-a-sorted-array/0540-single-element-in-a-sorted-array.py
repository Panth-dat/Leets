class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1 or nums[0]!=nums[1]:
            return nums[0]
        elif nums[-1]!=nums[-2]:
            return nums[-1]
        l=1
        r=len(nums)-2
        while l<=r:
            mid=(l+r)//2
            if (nums[mid]!=nums[mid + 1]) and (nums[mid]!=nums[mid - 1]):
                return nums[mid]
            elif (mid % 2==0 and nums[mid]==nums[mid+1]) or (mid % 2==1 and nums[mid]==nums[mid-1]):
                l=mid+1
            else:
                r=mid-1
