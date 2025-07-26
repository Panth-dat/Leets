class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        import numpy
        return numpy.base_repr(num, base=7)