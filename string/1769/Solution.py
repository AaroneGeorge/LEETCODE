class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """

        l = []
        for i in range(0,len(boxes)):

            number_of_operations = 0        
            for j in range(0,len(boxes)):
                if boxes[j] == "1":
                    number_of_operations += abs(i-j)
            
            l.append(number_of_operations)
        
        print(l)
    
s = Solution()
s.minOperations("001011")
