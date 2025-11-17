class Solution(object):
    def minLengthAfterRemovals(self, s):
        """
        :type s: str
        :rtype: int
        """
        x=s.count('a')
        y=s.count('b')
        if x>y:
            return x-y
        elif x<y:
            return y-x
        else:
            return 0