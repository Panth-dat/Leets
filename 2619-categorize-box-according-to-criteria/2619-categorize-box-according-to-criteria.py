class Solution(object):
    def categorizeBox(self, length, width, height, mass):
        """
        :type length: int
        :type width: int
        :type height: int
        :type mass: int
        :rtype: str
        """
        v=length*width*height
        if mass>=10**4 or length>=10**4 or width>=10**4 or height>=10**4 or v>=10**9:
            a="Bulky"
        else:
            a=0
        if mass>=100:
            b="Heavy"
        else:
            b=0
        if a=="Bulky" and b=="Heavy":
            return "Both"
        elif a==0 and b==0:
            return "Neither"
        elif a=="Bulky" and b==0:
            return "Bulky"
        else:
            return "Heavy"