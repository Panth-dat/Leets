class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq={}
        for c in s:
            freq[c]=freq.get(c,0)+1
        stack=[]
        vis=set()
        for i in s:
            freq[i]-=1
            if i in vis:
                continue
            while stack and i<stack[-1] and freq[stack[-1]]>0:
                vis.remove(stack.pop())
            stack.append(i)
            vis.add(i)
        return "".join(stack)