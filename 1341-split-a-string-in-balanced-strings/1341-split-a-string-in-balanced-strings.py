class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        x=0
        c=0
        for i in range(len(s)):
            if s[i]=='L':
                x+=1
            else:
                x-=1
            if x==0:
                c+=1
        return c