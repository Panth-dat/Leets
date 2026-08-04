class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ans=[]
        nums=sorted(nums)
        for i in range(nums[0],nums[-1]):
            if i not in nums:
                ans.append(i)
        return ans