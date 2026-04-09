class Solution(object):
    def minAbsoluteDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        diffs=[]
        indices1 = [i for i, x in enumerate(nums) if x == 1]
        indices2 = [j for j, y in enumerate(nums) if y == 2]
        if (not indices1) or (not indices2):
            return -1
        else:
            for z in indices1:
                for a in indices2:
                    diff=abs(z-a)
                    diffs.append(diff)
            return min(diffs)
