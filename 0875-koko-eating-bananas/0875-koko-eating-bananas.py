class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles)==h:
            return max(piles)
        def hrsink(piles, k):
            hr=0
            for i in range(len(piles)):
                x=piles[i]//k
                if (piles[i]%k)!=0:
                    x+=1
                hr+=x
            return hr
        l=1
        r=max(piles)
        while l<r:
            m=(l+r)//2
            if hrsink(piles, m)<=h:
                r=m
            else:
                l=m + 1
        return l