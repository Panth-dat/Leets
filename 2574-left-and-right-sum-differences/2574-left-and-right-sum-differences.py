class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        i=0
        ans=[]
        while i<len(nums):
            lsum=sum(nums[0:i])
            rsum=sum(nums[i+1:])
            if lsum>=rsum:
                x=lsum-rsum
                i+=1
            else:
                x=rsum-lsum
                i+=1
            ans.append(x)
        return ans