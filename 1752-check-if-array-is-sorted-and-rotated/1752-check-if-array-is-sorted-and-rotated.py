class Solution:
    def check(self, nums: List[int]) -> bool:
        n=len(nums)
        c=0
        for i in range(n-1):
            if nums[i+1]<nums[i]:
                c+=1
        if nums[-1]>nums[0]:
            c+=1
        return c<=1