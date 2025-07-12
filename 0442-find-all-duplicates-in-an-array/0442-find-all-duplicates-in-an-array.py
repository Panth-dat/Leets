class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=len(nums)
        x=[]
        nums.sort()
        for i in range(1,a):
            if nums[i]==nums[i-1]:
                x.append(nums[i])
        return x             
