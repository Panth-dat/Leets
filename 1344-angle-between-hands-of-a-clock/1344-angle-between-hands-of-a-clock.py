class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minang=minutes*6
        hrang=hour*30+((minutes)*0.5)
        if hrang>=360:
            hrang=hrang-360
        ans=minang-hrang
        if ans<0:
            ans=-ans
        if ans>180:
            ans=360-ans
        return ans