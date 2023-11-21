class Solution(object):
    def maximumStrongPairXor(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        for i in nums:
            for j in nums:
                if abs(i-j) <= min(i,j):
                    print(i,",",j)
                    if c < i^j:
                        c = i^j
        
        print(c)

s = Solution()
s.maximumStrongPairXor([1,2,3,4,5])