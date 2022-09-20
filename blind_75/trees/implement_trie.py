import time


class Trie:

    def __init__(self):
        self.children = {}
        self.is_word = False

    def insert(self, word: str) -> None:
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
        curr.is_word = True

    def search(self, word: str) -> bool:
        curr = self
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return curr.is_word

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for c in prefix:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return True


if __name__ == '__main__':
    trie = Trie()

    start_time = time.time()
    trie.insert('apple')
    trie.insert('appa')
    trie.insert('app')
    print(Trie)
    print(trie.search('apple'))
    print(trie.search('app'))
    print(trie.startsWith('app'))
    print("----%s seconds----" % (time.time() - start_time))
