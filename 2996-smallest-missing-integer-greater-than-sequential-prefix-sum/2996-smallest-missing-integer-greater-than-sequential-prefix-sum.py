class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        ans=nums[0]
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]+1:
                break
            ans+=nums[i]
        nums=set(nums)
        while ans in nums:
            ans+=1
        return ans