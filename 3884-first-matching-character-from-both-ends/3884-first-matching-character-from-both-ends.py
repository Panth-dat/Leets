class Solution(object):
    def firstMatchingIndex(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        x=-1
        for i in range(n):
            if s[i]==s[n-i-1]:
                x=i
                break
        return x