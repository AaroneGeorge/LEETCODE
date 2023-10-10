class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        val = 0
        for i in operations:
            if "+" in i:
                val += 1
            elif "-" in i:
                val -= 1
        
        print(val)

s = Solution()
s.finalValueAfterOperations(["--X","X++","X++"])
s.finalValueAfterOperations(["++X","++X","X++"])
s.finalValueAfterOperations(["X++","++X","--X","X--"])
