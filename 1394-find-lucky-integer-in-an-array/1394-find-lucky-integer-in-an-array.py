from collections import Counter
class Solution:
    def findLucky(self, arr: list[int]) -> int:
        a=-1
        x=Counter(arr)
        for i,j in x.items():
            if i==j and i>a:
                a=i
        return a