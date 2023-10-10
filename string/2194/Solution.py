import re

class Solution(object):
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        c1, c2 = ord(s[0]), ord(s[3])
        r1, r2 = int(s[1]), int(s[4])
        print( [chr(c) + str(r) for c in range(c1, c2 + 1) for r in range(r1, r2 + 1)] )

s = Solution()
s.cellsInRange("U7:X9")
        