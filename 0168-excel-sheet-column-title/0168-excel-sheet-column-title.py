class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        ans = ''
        while columnNumber > 0:
              columnNumber -= 1 
              ans += chr(ord('A') + columnNumber % 26)
              columnNumber /= 26
            
        
        return ans[::-1]