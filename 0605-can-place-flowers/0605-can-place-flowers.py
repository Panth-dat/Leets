class Solution:
    def canPlaceFlowers(self, x: List[int], n: int) -> bool:
        c=0
        i=0
        while i<len(x):
            if (x[i] == 0 and (i == 0 or x[i-1] == 0) and (i == len(x)-1 or x[i+1] == 0)):
                c+=1
                i+=1
            i+=1
        return (c>=n)