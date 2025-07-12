class Solution(object):
    def generateTag(self, caption):
        """
        :type caption: str
        :rtype: str
        """
        words=caption.split()
        result="#"
        for i,words in enumerate(words):
            if i==0:
                result+=words.lower()
            else:
                result+=words[0].upper()+words[1:].lower()
        result=result[:100]
        return result