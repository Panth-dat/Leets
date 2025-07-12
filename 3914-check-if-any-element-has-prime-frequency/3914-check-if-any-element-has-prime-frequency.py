from collections import Counter

class Solution(object):
    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(sqrt(n))+ 1):
            if n % i == 0:
                return False
        return True

    def checkPrimeFrequency(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = Counter(nums)
        for freq in count.values():
            if self.is_prime(freq):
                return True
        return False
