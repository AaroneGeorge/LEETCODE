class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        max = 0
        for i in sentences:
            l = i.split()
            if max < len(l):
                max = len(l)

        print(max)

s = Solution()
s.mostWordsFound(["please wait", "continue to fight", "continue to win"])