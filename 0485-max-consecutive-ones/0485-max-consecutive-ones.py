class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        x=0
        for i in range(len(nums)):
            if nums[i]==0:
                c=0
            else:
                c+=1
                x=max(c,x)
        return x