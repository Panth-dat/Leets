class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        c,d,e=0,0,0
        for i in range(len(nums)):
            if nums[i]==0:
                c+=1
            elif nums[i]==1:
                d+=1
            else:
                e+=1
        x=0
        for _ in range(c):
            nums[x]=0
            x+=1
        for _ in range(d):
            nums[x]=1
            x+=1
        for _ in range(e):
            nums[x]=2
            x+=1