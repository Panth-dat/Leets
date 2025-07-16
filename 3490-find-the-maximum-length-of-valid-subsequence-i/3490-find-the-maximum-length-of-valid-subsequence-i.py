class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        odd = 0
        change = 0

        for i in range(n):
            if nums[i] % 2 != 0:
                odd += 1

            if i > 0 and (nums[i] + nums[i - 1]) % 2 != 0:
                change += 1

        even = n - odd
        return max(change + 1, max(odd, even))