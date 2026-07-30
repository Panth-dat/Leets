class Solution:
    def minimumPushes(self, word: str) -> int:
        x=len(word)
        if x<=8:
            return x
        elif x<=16:
            return 2*(x-4)
        elif x<=24:
            return 3*(x-8)
        else:
            return 4*(x-12)