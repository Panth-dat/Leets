class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        # Calculate the expected sum of consecutive integers from 0 to n
        expected_sum = n * (n + 1) // 2
        
        # Calculate the actual sum of the elements in the array
        actual_sum = sum(nums)
        
        # The missing number is the difference between the expected sum and the actual sum
        return expected_sum - actual_sum