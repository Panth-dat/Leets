class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        c=0
        ans=0
        for i in nums:
            if i==0:
                c+=1
                ans+=c
            else:
                c=0
        return ans