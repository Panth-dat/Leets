class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        st1=Counter(ransomNote)
        st2=Counter(magazine)
        if st1-st2=={}:
            return True
        else:
            return False