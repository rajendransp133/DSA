class Trie:

    def __init__(self):
        self.array=[]
        

    def insert(self, word: str) -> None:
        self.array.append(word)
        

    def search(self, word: str) -> bool:
        return True if(word in self.array) else False
        

    def startsWith(self, prefix: str) -> bool:
        n=len(prefix)
        for i in self.array:
            if(i[:n]==prefix):
                return True
        return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)