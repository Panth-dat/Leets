class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        x=bin(n)[2:].zfill(32)
        y=x[::-1]
        return int(y,2)
        