class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        x=0
        for x in range(len(matrix)):           
            b,e=0,len(matrix[x])-1
            while b<=e:
                mid=(b+e)//2
                if matrix[x][mid]==target:
                    return True
                elif matrix[x][mid]<target:
                    b=mid+1
                else:
                    e=mid-1
        return False