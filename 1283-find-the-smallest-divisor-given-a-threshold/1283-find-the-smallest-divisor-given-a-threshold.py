class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def suum(nums, k):
            x=0
            for i in range(len(nums)):
                x+=math.ceil(nums[i]/k)
            return x
        l=1
        r=max(nums)
        while l<r:
            m=(l+r)//2
            x=suum(nums, m)
            if x<=threshold:
                r=m
            else:
                l=m + 1
        return l