class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        x=max(arr)
        y=len(arr)
        if y<3:
            return False
        else:
            i=0
            while arr[i]<x:
                if arr[i]>=arr[i+1]:
                    return False
                    break
                else:
                    i+=1
            if i==0 or i==(y-1):
                return False
            while i<(y-1):
                if arr[i]<=arr[i+1]:
                    return False
                    break
                else:
                    i+=1
            return True