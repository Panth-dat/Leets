class Solution:
    def greatestLetter(self, s: str) -> str:
        s=set(s)
        s=str(s)
        ans=""
        for i in range(len(s)):
            if s[i].isupper() and (s[i].lower() in s) and s[i]>ans:
                ans=s[i]
            elif s[i].islower() and (s[i].upper() in s) and s[i]>ans:
                ans=s[i]
        return ans.upper()