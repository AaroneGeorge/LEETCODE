class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """        
        if "()" in command:
            command = command.replace("()","o")
        if "(al)" in command:
            command = command.replace("(al)","al")

        print(command)

s = Solution()
s.interpret("(al)G(al)()()G")