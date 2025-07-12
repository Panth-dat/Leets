class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i=0
        j=len(numbers)-1
        numbers.sort()
        while i<j:
            if numbers[i]+numbers[j]==target:
                return[i+1,j+1]
            elif numbers[i]+numbers[j]<target:
                i=i+1
            else:
                j=j-1