class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s1=''
        for x in s.lower():
            if x.isalnum():
                s1+=x
        if s1==s1[::-1]:
            return True
        else:
            return False