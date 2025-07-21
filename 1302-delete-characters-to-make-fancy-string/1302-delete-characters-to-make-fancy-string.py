class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        x = []
        if len(s) < 3:
            return s
        x.append(s[0])
        x.append(s[1])
        for i in range(2, len(s)):
            if not (s[i] == x[-1] == x[-2]):
                x.append(s[i])
        return ''.join(x)