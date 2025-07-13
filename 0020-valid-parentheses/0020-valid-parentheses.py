class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        if len(s)%2!=0:
            return False
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                stack.append(s[i])
            elif s[i]==')'and stack and stack[-1]=='(':
                stack.pop()
            elif s[i]==']'and stack and stack[-1]=='[':
                stack.pop()
            elif s[i]=='}'and stack and stack[-1]=='{':
                stack.pop()
            else:
                return False
        return len(stack)==0
