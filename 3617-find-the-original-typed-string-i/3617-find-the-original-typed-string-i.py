class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        c=1
        for i in range(len(word)-1):
            if word[i]==word[i+1]:
                c+=1
        return c