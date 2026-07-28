from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = Counter(s)

        mid=""
        right=[]

        for ch in sorted(freq.keys(), reverse=True):
            if freq[ch]%2==1:
                mid=ch
            right.append(ch*(freq[ch]//2))

        right="".join(right)
        left=right[::-1]

        return left+mid+right