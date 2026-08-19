class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        i=0
        while x!=0 and y>=4:
            i+=1
            x-=1
            y-=4
        if i%2==0:
            return "Bob"
        else:
            return "Alice"