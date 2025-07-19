class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        arr = list(t)
        for i in range(len(s)):
            arr.remove(s[i])
        return arr[0]