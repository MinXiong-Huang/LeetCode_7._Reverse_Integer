import math

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        def cmp(a, b):
            return (a > b) - (a < b) 

        rev_x = int(str(abs(x))[::-1])
        if rev_x > math.pow(2, 31):
            return 0
        else:
            return rev_x * cmp(x, 0)

#Example
s=Solution()
s.reverse(-123)