class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        Area=0
        i=0
        j=len(height)-1
        while i<j:
            a=height[i]
            b=height[j]
            if a<=b:
                area=(j-i)*a
                i=i+1
            else:
                area=(j-i)*b
                j=j-1
            if area>Area:
                Area=area
        return Area