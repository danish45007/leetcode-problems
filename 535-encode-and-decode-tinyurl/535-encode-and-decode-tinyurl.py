class Codec:
    def __init__(self):
        self.encode_url_map = {}
        self.decode_url_map = {}
        self.short_base_url = 'https://tinyurl.com'
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.encode_url_map:
            short_url = self.short_base_url + str(len(self.encode_url_map) + 1)
            self.encode_url_map[longUrl] = short_url
            self.decode_url_map[short_url] = longUrl
        return self.encode_url_map[longUrl]
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        if shortUrl in self.decode_url_map:
            return self.decode_url_map[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))