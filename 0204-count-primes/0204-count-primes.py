class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

        i = 2
        while i * i < n:
            if is_prime[i]:
                for j in range(i * i, n, i):  # Start from i*i
                    is_prime[j] = False
            i += 1

        return sum(is_prime)
