class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        c,x=0,0
        if len(word)<3:
            return False
        v='aeiouAEIOU'
        n='0123456789'
        if word.isalnum():
            for i in range(len(word)):
                if word[i] in v:
                    c=1
                if word[i] not in v and word[i] not in n:
                    x=1
        if c==1 and x==1:
            return True
        else:
            return False
