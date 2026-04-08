class Solution(object):
    def firstUniqueEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=-1
        for i in range(len(nums)):
            if (nums[i]%2==0) and (nums.count(nums[i])==1):
                x = nums[i]
                break
        return x