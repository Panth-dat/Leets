class Solution(object):
    def fairCandySwap(self, a, b):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        val=(sum(a)-sum(b))//2
        for i in b:
            if i+val in a:
                return [i+val, i]