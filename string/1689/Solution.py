class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """

        self.n = n
        n = self.n

        max = 0
        for i in n:
            if int(i) > max:
                max = int(i)
        
        print(max)

s= Solution()
s.minPartitions("32")
s.minPartitions("82734")
s.minPartitions("27346209830709182346")