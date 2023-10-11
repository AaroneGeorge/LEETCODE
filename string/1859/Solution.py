class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = {}
        s1 = ""
        for i in s.split():
            d[i[-1]] = i[:-1] 

        for j in range(len(d)):
            for i in d:
                if int(i) == j+1:
                    s1 += d[i]
            s1 += " "
        print(s1[:-1])

s = Solution()
s.sortSentence("Myself2 Me1 I4 and3")