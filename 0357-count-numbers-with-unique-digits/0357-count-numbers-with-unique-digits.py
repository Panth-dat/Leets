class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        if n == 0:
            return 1
        ans = 10
        ud = 9
        ad = 9
        for i in range(2, n + 1):
            ud *= ad
            ans += ud
            ad -= 1
        return ans