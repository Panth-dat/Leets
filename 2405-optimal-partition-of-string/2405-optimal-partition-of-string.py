class Solution:
    def partitionString(self, s: str) -> int:
        c=1
        x=[]
        for i in s:
            if i not in x:
                x.append(i)
            else:
                x=[i]
                c+=1
        return c