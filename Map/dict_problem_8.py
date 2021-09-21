################################################################
# Leet Code: https://leetcode.com/problems/encode-and-decode-tinyurl/
# DS: Dictonary
# Problem Number: 8
################################################################
#---------------------------------------------------------------
### Encode
#  1. Convert the input string into a hash and store the hap as key in dict
#  2. Place the url value for the hash ket created
#  3. Return the ke value by attaching it to tiny-url
### Decode
#  1. Take in the tiny url - decode the hash from the string
#  2. Pass the hash into the comman map to search for the url
#  3. Return the retrived URL
#---------------------------------------------------------------
class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.map_1 = {}
        self.map_1[abs(hash(longUrl))] = longUrl
        #print(self.map_1)
        shortUrl = 'http://tinyurl.com/'+str(abs(hash(longUrl)))
        print(shortUrl)
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        print(shortUrl)
        key = int(shortUrl.strip('http://tinyurl.com/'))
        print(key)
        value = self.map_1[key]
        return value
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
