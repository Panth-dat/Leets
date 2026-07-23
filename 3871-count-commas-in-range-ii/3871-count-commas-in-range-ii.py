class Solution:
    def countCommas(self, n: int) -> int:
        c=0
        nc=[10**3,10**6,10**9,10**12,10**15]
        for i in nc:
            if n>=i:
                c+=(n-i+1)
        return c
        