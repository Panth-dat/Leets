from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cntele=Counter(nums)
        ans=[]
        return sorted(cntele,key=cntele.get,reverse=True)[:k]       