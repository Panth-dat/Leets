class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if max(nums)==min(nums):
            return 0
        else:
            return 1