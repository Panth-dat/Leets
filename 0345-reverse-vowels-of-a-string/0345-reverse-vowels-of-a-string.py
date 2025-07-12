class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels=set("aeiouAEIOU")
        s=list(s)
        i=0
        j=len(s)-1
        while i<j:
            if (s[i] in vowels) and (s[j] in vowels):
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
            elif (s[i] in vowels) and (s[j] not in vowels):
                j-=1
            elif (s[i] not in vowels) and (s[j] in vowels):
                i+=1
            else:
                i+=1
                j-=1
        return "".join(s)
            