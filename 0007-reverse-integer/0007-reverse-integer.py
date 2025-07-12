class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y=x
        rtype=0
        if (x<0):
            x=-x
        while(x>0):
            dig=x%10
            rtype=rtype*10+dig
            x=x//10
        if (rtype<2147483647 and rtype>-2147483648):
            if (y<0):
                return -rtype
            else :     
                return rtype
        else :
            return 0   