class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1=[]
        num2=[]
        for i in range(1,n+1):
            if i%m==0:
                num2.append(i)
            else:
                num1.append(i)
        num1=sum(num1)
        num2=sum(num2)
        return num1-num2