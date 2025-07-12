class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = 1
        nums = set(nums)
        while True:
            if num not in nums:
                return num
            num += 1