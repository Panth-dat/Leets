class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        i=0
        j=i
        for x in nums:
            if i<=x:
                j=i
                i=x
            elif j<=x:
                j=x
        return (i-1)*(j-1)