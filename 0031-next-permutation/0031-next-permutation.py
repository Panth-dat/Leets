class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) == 1:
            return
        n = len(nums)
        for j in range(n - 2, -1, -1):
            for i in range(n - 1, j, -1):
                if nums[i] > nums[j]:
                    nums[j], nums[i] = nums[i], nums[j]
                    nums[j + 1:] = reversed(nums[j + 1:])
                    return

        nums.reverse()