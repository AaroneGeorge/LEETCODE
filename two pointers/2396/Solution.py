class Solution(object):
    def isStrictlyPalindromic(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        for i in range(2,n-1):
            temp = n
            s=''
            while temp != 0:
                s += str(temp % i)
                temp /= i

            if s == s[::-1]:
                check = 1
            else:
                check = 0
                break

        if check == 1:
            print(True)
        else:
            print(False)
            
s = Solution()
s.isStrictlyPalindromic(9)