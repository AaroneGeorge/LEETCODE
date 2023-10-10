class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        
        alpha = "abcdefghijklmnopqrstuvwxyz"
        
        string = key.replace(" ","")

        s = ""

        for char in string:
            if char not in s:
                s += char

        for i in range(len(message)):
            if message[i].isalpha():
                c = alpha[s.find(message[i])]
                message = message[:i] + c + message[i+1:]

        print(message)

s = Solution()
s.decodeMessage("eljuxhpwnyrdgtqkviszcfmabo","zwx hnfx lqantp mnoeius ycgk vcnjrdb")