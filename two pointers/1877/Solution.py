class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            for j in range(len(nums) - i -1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
        
        i=0
        j = len(nums)-1
        c = nums[i] + nums[j]
        
        for i in range(j):
            if c < nums[i] + nums[j]:
                c = nums[i] + nums[j]
            j-=1


        print(c)

s = Solution()
s.minPairSum([3,5,4,2,4,6])