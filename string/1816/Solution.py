class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        s = s.split()
        s = s[:k]

        print(" ".join(s))

s = Solution()
s.truncateSentence("Hello how are you Contestant",4)