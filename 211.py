import collections


class WordDictionary:

    def __init__(self):
        self.children = collections.defaultdict(TrieNode)

    def addWord(self, word: str) -> None:
        cur = self
        for c in word:
            cur = cur.children[c]

        cur.isWord = True

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return False

        return iterSearch(self.children, word)


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return self.isWord

        return iterSearch(self.children, word)


def iterSearch(children: dict, word: str) -> bool:
    cur = word[0]
    if cur == '.':
        for c in children.values():
            if c.search(word[1:]):
                return True

        return False

    if cur not in children:
        return False

    return children[cur].search(word[1:])
