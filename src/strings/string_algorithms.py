"""
Module: string_algorithms.py  Topic: Strings
Sliding window, two pointers, KMP, anagram, palindrome, Rabin-Karp.
"""
from typing import List, Optional
from collections import Counter, defaultdict


def longest_substring_no_repeat(s: str) -> int:
    """Longest substring without repeating chars. O(n).
    >>> longest_substring_no_repeat("abcabcbb")
    3
    """
    seen: dict = {}; l = best = 0
    for r, c in enumerate(s):
        if c in seen and seen[c] >= l: l = seen[c]+1
        seen[c] = r; best = max(best, r-l+1)
    return best


def min_window_substring(s: str, t: str) -> str:
    """Minimum window containing all chars of t. O(|s|+|t|).
    >>> min_window_substring("ADOBECODEBANC","ABC")
    'BANC'
    """
    need = Counter(t); have, total = 0, len(need)
    res, res_len = [-1,-1], float("inf")
    window: dict = {}; l = 0
    for r, c in enumerate(s):
        window[c] = window.get(c,0)+1
        if c in need and window[c] == need[c]: have += 1
        while have == total:
            if r-l+1 < res_len: res=[l,r]; res_len=r-l+1
            window[s[l]] -= 1
            if s[l] in need and window[s[l]] < need[s[l]]: have -= 1
            l += 1
    l, r = res
    return s[l:r+1] if res_len != float("inf") else ""


def is_anagram(s: str, t: str) -> bool:
    """Check anagram using frequency counts. O(n).
    >>> is_anagram("anagram","nagaram")
    True
    """
    return Counter(s) == Counter(t)


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """Group anagrams together. O(n*k logk).
    >>> len(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
    3
    """
    groups: dict = defaultdict(list)
    for s in strs: groups[tuple(sorted(s))].append(s)
    return list(groups.values())


def is_palindrome_str(s: str) -> bool:
    """Alphanumeric palindrome check. O(n).
    >>> is_palindrome_str("A man a plan a canal Panama")
    True
    """
    s = "".join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]


def longest_palindromic_substring(s: str) -> str:
    """Expand-around-center. O(n^2) time, O(1) space.
    >>> longest_palindromic_substring("babad") in ["bab","aba"]
    True
    """
    res = ""
    def expand(l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]: l -= 1; r += 1
        return s[l+1:r]
    for i in range(len(s)):
        odd = expand(i, i); even = expand(i, i+1)
        if len(odd) > len(res): res = odd
        if len(even) > len(res): res = even
    return res


def kmp_search(text: str, pattern: str) -> List[int]:
    """Knuth-Morris-Pratt pattern search. O(n+m).
    >>> kmp_search("AABAACAADAABAABA","AABA")
    [0, 9, 12]
    """
    if not pattern: return []
    def build_lps(p: str) -> List[int]:
        lps = [0]*len(p); l = 0; i = 1
        while i < len(p):
            if p[i] == p[l]: l += 1; lps[i] = l; i += 1
            elif l: l = lps[l-1]
            else: lps[i] = 0; i += 1
        return lps
    lps = build_lps(pattern); res: List[int] = []; i = j = 0
    while i < len(text):
        if text[i] == pattern[j]: i += 1; j += 1
        if j == len(pattern): res.append(i-j); j = lps[j-1]
        elif i < len(text) and text[i] != pattern[j]:
            if j: j = lps[j-1]
            else: i += 1
    return res


def count_palindromic_substrings(s: str) -> int:
    """Count all palindromic substrings. O(n^2).
    >>> count_palindromic_substrings("aaa")
    6
    """
    count = 0
    def expand(l: int, r: int) -> None:
        nonlocal count
        while l >= 0 and r < len(s) and s[l] == s[r]: count += 1; l -= 1; r += 1
    for i in range(len(s)): expand(i, i); expand(i, i+1)
    return count


def longest_common_prefix(strs: List[str]) -> str:
    """Longest common prefix. O(S).
    >>> longest_common_prefix(["flower","flow","flight"])
    'fl'
    """
    if not strs: return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix): prefix = prefix[:-1]
        if not prefix: return ""
    return prefix


def reverse_words(s: str) -> str:
    """Reverse words in string. O(n).
    >>> reverse_words("the sky is blue")
    'blue is sky the'
    """
    return " ".join(s.split()[::-1])


def encode(strs: List[str]) -> str:
    """Encode list of strings to single string."""
    return "".join(f"{len(s)}#{s}" for s in strs)


def decode(s: str) -> List[str]:
    """Decode encoded string back to list."""
    res: List[str] = []; i = 0
    while i < len(s):
        j = s.index("#", i); length = int(s[i:j])
        res.append(s[j+1:j+1+length]); i = j+1+length
    return res


def check_inclusion(s1: str, s2: str) -> bool:
    """Check if any permutation of s1 is substring of s2. O(n).
    >>> check_inclusion("ab","eidbaooo")
    True
    """
    if len(s1) > len(s2): return False
    c1, c2 = Counter(s1), Counter(s2[:len(s1)])
    if c1 == c2: return True
    for i in range(len(s1), len(s2)):
        c2[s2[i]] += 1
        old = s2[i-len(s1)]
        c2[old] -= 1
        if c2[old] == 0: del c2[old]
        if c1 == c2: return True
    return False


if __name__ == "__main__":
    print("No repeat:", longest_substring_no_repeat("abcabcbb"))
    print("Min window:", min_window_substring("ADOBECODEBANC","ABC"))
    print("Anagram:", is_anagram("anagram","nagaram"))
    print("Groups:", len(group_anagrams(["eat","tea","tan","ate","nat","bat"])))
    print("Palindrome:", is_palindrome_str("A man a plan a canal Panama"))
    print("Longest palindrome:", longest_palindromic_substring("babad"))
    print("KMP:", kmp_search("AABAACAADAABAABA","AABA"))
    print("Palindrome count:", count_palindromic_substrings("aaa"))
    print("Common prefix:", longest_common_prefix(["flower","flow","flight"]))
    print("Check inclusion:", check_inclusion("ab","eidbaooo"))
