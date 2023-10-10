class Solution(object):
    def defangIPaddr(self, address):
        self.address = address
        a = self.address

        new = a.replace(".","[.]")
        
        print(new)

s = Solution()
s.defangIPaddr("1.1.1.1")