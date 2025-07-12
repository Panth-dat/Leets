class Solution(object):
    def longestString(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        if x>y:
            return 2*(y+1)+2*y+2*z
        elif y>x:
            return 2*x+2*(x+1)+2*z
        else:
            return 2*x+2*y+2*z