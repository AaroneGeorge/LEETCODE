class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        no = 0
        l = 0
        r = 0
        for i in s:
            if i =="L":
                l += 1
            
            if i == "R":
                r += 1

            if l==r:
                no += 1
                l=0
                r=0

        print(no)

s = Solution()
s.balancedStringSplit("RLRRLLRLRL")