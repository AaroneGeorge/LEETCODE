class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        c=0
        for i in range(len(s)-2):
            j = s[i:3+i]
            if len(set(j)) == len(j):
                c+=1       
        print(c)
    

s = Solution()
s.countGoodSubstrings("aababcabc")