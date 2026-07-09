class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans=[]
        x=0
        for i in nums:
            x=(2*x + i)%5
            ans.append(x==0)
        return ans