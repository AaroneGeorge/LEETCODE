class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        for i in range(len(s)):
            s[i] = s[i][::-1]

        print(" ".join(s))

s = Solution()
s.reverseWords("Let's take LeetCode contest")