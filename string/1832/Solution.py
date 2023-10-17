class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        if len(set(sentence.lower())) == 26:
            print(True)
        else:
            print(False)

        

s = Solution()
s.checkIfPangram("thequickbrownfoxjumpsoverthelazydog")