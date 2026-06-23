"""
Module: trie.py  Topic: Trie (Prefix Tree)
Trie with insert, search, startsWith, delete, autocomplete.
WordDictionary with wildcard. Replace words.
"""
from typing import Optional, List, Dict


class TrieNode:
    def __init__(self) -> None:
        self.children: Dict[str, "TrieNode"] = {}
        self.is_end: bool = False
        self.count: int = 0


class Trie:
    """Prefix Tree. All ops O(L). Space O(sum of all chars).
    >>> t=Trie(); t.insert("apple"); t.search("apple")
    True
    """
    def __init__(self) -> None: self.root = TrieNode()

    def insert(self, word: str) -> None:
        n = self.root
        for c in word:
            if c not in n.children: n.children[c] = TrieNode()
            n = n.children[c]; n.count += 1
        n.is_end = True

    def search(self, word: str) -> bool:
        n = self._go(word)
        return n is not None and n.is_end

    def starts_with(self, prefix: str) -> bool:
        return self._go(prefix) is not None

    def _go(self, s: str) -> Optional[TrieNode]:
        n = self.root
        for c in s:
            if c not in n.children: return None
            n = n.children[c]
        return n

    def count_prefix(self, prefix: str) -> int:
        n = self._go(prefix); return n.count if n else 0

    def delete(self, word: str) -> bool:
        def _del(n: TrieNode, w: str, i: int) -> bool:
            if i == len(w):
                if not n.is_end: return False
                n.is_end = False; return len(n.children) == 0
            c = w[i]
            if c not in n.children: return False
            if _del(n.children[c], w, i+1):
                del n.children[c]; return not n.is_end and len(n.children) == 0
            return False
        return _del(self.root, word, 0)

    def autocomplete(self, prefix: str) -> List[str]:
        n = self._go(prefix)
        if not n: return []
        res: List[str] = []
        def dfs(node: TrieNode, path: List[str]) -> None:
            if node.is_end: res.append(prefix + "".join(path))
            for c, child in sorted(node.children.items()):
                path.append(c); dfs(child, path); path.pop()
        dfs(n, []); return res

    def all_words(self) -> List[str]: return self.autocomplete("")


class WordDictionary:
    """Trie supporting '.' wildcard in search.
    >>> wd=WordDictionary(); wd.add_word("bad"); wd.search(".ad")
    True
    """
    def __init__(self) -> None: self.root = TrieNode()

    def add_word(self, w: str) -> None:
        n = self.root
        for c in w:
            if c not in n.children: n.children[c] = TrieNode()
            n = n.children[c]
        n.is_end = True

    def search(self, w: str) -> bool:
        def dfs(n: TrieNode, i: int) -> bool:
            if i == len(w): return n.is_end
            c = w[i]
            if c == ".": return any(dfs(ch, i+1) for ch in n.children.values())
            return c in n.children and dfs(n.children[c], i+1)
        return dfs(self.root, 0)


def replace_words(dictionary: List[str], sentence: str) -> str:
    """Replace words with shortest matching root.
    >>> replace_words(["cat","bat","rat"], "the cattle was rattled by the battery")
    'the cat was rat by the bat'
    """
    t = Trie()
    for root in dictionary: t.insert(root)
    def find_root(word: str) -> str:
        n = t.root
        for i, c in enumerate(word):
            if c not in n.children: break
            n = n.children[c]
            if n.is_end: return word[:i+1]
        return word
    return " ".join(find_root(w) for w in sentence.split())


if __name__ == "__main__":
    t = Trie()
    for w in ["apple","app","application","banana","band"]: t.insert(w)
    print("search apple:", t.search("apple"))
    print("search appl:", t.search("appl"))
    print("starts_with app:", t.starts_with("app"))
    print("autocomplete app:", t.autocomplete("app"))
    print("all words:", t.all_words())
    wd = WordDictionary()
    for w in ["bad","dad","mad"]: wd.add_word(w)
    print("search .ad:", wd.search(".ad"))
    print("search b..:", wd.search("b.."))
    print("replace_words:", replace_words(["cat","bat","rat"],"the cattle was rattled by the battery"))
