class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """

        res_string = ""

        for i in range(len(s)):
            for j in range(len(s)):
                if i==indices[j]:
                    res_string += s[j]

        print(res_string)
            

s = Solution()
s.restoreString("codeleet",[4,5,6,7,0,2,1,3])