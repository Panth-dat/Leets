class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1]:
            return letters[0]
        else:
            i=0
            while True:
                if target < letters[i]:
                    return letters[i]
                    break
                else:
                    i+=1