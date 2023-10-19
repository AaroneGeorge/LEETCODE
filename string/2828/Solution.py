class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        s1=""
        for i in words:
            s1 += i[0]
        
        print(s1==s)
    
s = Solution()
s.isAcronym(["alice","bob","charlie"],"abc")
s.isAcronym(["an","apple"],"a")