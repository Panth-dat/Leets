class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[x]=nums[i]
                x+=1
        return x

        