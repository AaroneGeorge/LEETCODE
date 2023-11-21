class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pnums = []
        nnums = []

        for i in nums:
            if i<0:
                nnums.append(i)
            else:
                pnums.append(i)

        rearrList = []
        for j in range(len(pnums)):
            rearrList.append(pnums[j])
            rearrList.append(nnums[j])

        print(rearrList)

s = Solution()
s.rearrangeArray([3,1,-2,-5,2,-4])