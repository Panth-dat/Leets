class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        fm=min(nums)
        sm=fm
        tm=sm
        fl=max(nums)
        sl=fl
        for i in range(len(nums)):
            if fm<=nums[i]:
                tm=sm
                sm=fm
                fm=nums[i]
            elif sm<=nums[i]:
                tm=sm
                sm=nums[i]
            elif tm<=nums[i]:
                tm=nums[i]
            if fl>=nums[i]:
                sl=fl
                fl=nums[i]
            elif sl>=nums[i]:
                sl=nums[i]
        return max(fm*sm*tm, fl*sl*fm)