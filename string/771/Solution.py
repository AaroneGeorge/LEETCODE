class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        count = 0
        for i in jewels:
            for j in stones:
                if i==j:
                    count +=1
        
        print(count)

s = Solution()
s.numJewelsInStones("aA","aAAbbbb")
s.numJewelsInStones("z","ZZ")