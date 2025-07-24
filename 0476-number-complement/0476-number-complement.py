class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        b=bin(num)
        binary=b[2:]
        x=''
        for i in binary:
            if i=='0':
                x+='1'
            else:
                x+='0'
        dec=int(x, 2)
        return dec