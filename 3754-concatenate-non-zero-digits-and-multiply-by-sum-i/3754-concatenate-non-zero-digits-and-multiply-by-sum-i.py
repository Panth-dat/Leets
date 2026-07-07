class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x=[]
        for i in str(n):
            if i!="0":
                x.append(i)
        if len(x)==0:
            return 0
        else:
            x="".join(x)
            sumx=sum(int(y) for y in x)
            return int(x)*sumx