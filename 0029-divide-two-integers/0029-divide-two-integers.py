class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend < 0) == (divisor < 0)
        
        #Now we've stored our sign in poistive variable so we make both numbers positive
        dividend, divisor = abs(dividend), abs(divisor)
        
        #This is the quotient
        ans = 0
        
        #Outer while loop which checks the lower multiples of divisor
        while dividend >= divisor:
            temp, i = divisor, 1
            
             #Inner while loop where values value of multiples of divisor keep doubling after each iteration for less number of operations
            while dividend >= temp:
                dividend -= temp
                
                ans += i #Storing the number of times number multiplied
                
                i <<= 1 #Doubling -- 1,2,4..
                
                temp <<= 1 #Doubling Divisor values -- x,2x,4x...
        
        #Re-assigning the sign to our answer
        if not positive:
            ans = -ans
            
        #Returning answer within range
        return min(max(-2147483648, ans), 2147483647)