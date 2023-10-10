class Codec:

    initialPart = ""

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        index = longUrl.find(".com/") + 5
        self.initialPart = longUrl[:index]

        cutPart = longUrl[index:]
        encoded = ""

        for i in cutPart:
            encoded += chr(ord(i)+3)

        return("http://tinyurl.com/"+encoded)


        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        index = shortUrl.find(".com/") + 5
        cutpart = shortUrl[index:]

        decoded = ""

        for i in cutpart:
            decoded += chr(ord(i)-3)

        return(self.initialPart+decoded)
        

# Your Codec object will be instantiated and called as such:
codec = Codec()

print(codec.decode(codec.encode("https://leetcode.com/problems/design-tinyurl")))