class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi=0
        if len(nums)<2:
            return 0
        else:
            nums.sort()
            for i in range(len(nums)-1):
                x=nums[i+1]-nums[i]
                if x>maxi:
                    maxi=x
            return maxi  