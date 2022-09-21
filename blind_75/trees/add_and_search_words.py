import time


class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_word = True

    def search(self, word: str) -> bool:
        return self.dfs(0, word, self.root)

    def dfs(self, idx: int, word: str, root: TrieNode) -> bool:
        cur = root

        for i in range(idx, len(word)):
            c = word[i]

            if c == '.':
                for child in cur.children.values():
                    if self.dfs(i + 1, word, child):
                        return True
                return False
            else:
                if c not in cur.children:
                    return False
                cur = cur.children[c]

        return cur.is_word


if __name__ == '__main__':
    trie = WordDictionary()

    start_time = time.time()
    print("----%s seconds----" % (time.time() - start_time))
