class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        dig=[]
        for d in str(n):
            dig.append(int(d))
        dig.sort()
        return dig[-1]*dig[-2]