class Solution:
    def countPairs(self, nums, target):
        n=len(nums)
        ans=0
        for i in range(n):
            for j in range(i,n):
                if i<j and nums[i]+nums[j]<target:
                    ans+=1

        print(ans)

s = Solution()
s.countPairs([-1,1,2,3,1],2)   