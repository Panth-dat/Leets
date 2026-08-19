class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        ans=min(divisors)
        c=0
        max_s=-1
        for i in divisors:
            c=0
            for j in nums:
                if j%i==0:
                    c+=1
            if c>max_s:
                max_s=c
                ans=i
            elif c==max_s:
                ans=min(i,ans)
        return ans