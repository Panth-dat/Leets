class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        x=set('qwertyuiopQWERTYUIOP')
        y=set('asdfghjklASDFGHJKL')
        z=set('zxcvbnmZXCVBNM')
        ans=[]
        for i in range(len(words)):
            if (set(words[i]) <= x) or (set(words[i]) <= y) or (set(words[i]) <= z):
                ans.append(words[i])
        return ans