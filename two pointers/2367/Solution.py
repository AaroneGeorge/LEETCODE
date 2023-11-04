class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        c = 0

        for i in nums:
            for j in nums:
                for k in nums:
                    if j-k == diff:
                        if i-j == diff:
                            c += 1
                
        
        print(c)

s = Solution()
s.arithmeticTriplets([0,1,4,6,7,10],3)