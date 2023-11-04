class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """

        l1 = []
        l2 = []
        c=0

        for i in nums:
            if i < pivot:
                l1.append(i)
            if i > pivot:
                l2.append(i)
            if i == pivot:
                c+=1

        for i in range(c):
            l1.append(pivot)

        for i in l2:
            l1.append(i)


        print(l1)

s = Solution()
s.pivotArray([9,12,5,10,14,3,10],10)