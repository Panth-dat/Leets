class Solution:
    def integerBreak(self, n: int) -> int:
        ans=1
        if n==2:
            return 1
        if n==3:
            return 2
        while n>4:
            ans*=3
            n=n-3
        return ans*n