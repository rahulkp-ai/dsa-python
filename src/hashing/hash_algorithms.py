"""
Module: hash_algorithms.py  Topic: Hashing
HashMap patterns: LRU Cache, subarray sum k, top-k,
longest consecutive, contains duplicate.
"""

from collections import Counter, defaultdict
from typing import List, Optional


def contains_duplicate(nums: List[int]) -> bool:
    """O(n) time, O(n) space.
    >>> contains_duplicate([1,2,3,1])
    True
    """
    return len(nums) != len(set(nums))


def longest_consecutive(nums: List[int]) -> int:
    """Longest consecutive sequence. O(n).
    >>> longest_consecutive([100,4,200,1,3,2])
    4
    """
    num_set = set(nums)
    best = 0
    for n in num_set:
        if n - 1 not in num_set:
            cur, length = n, 1
            while cur + 1 in num_set:
                cur += 1
                length += 1
            best = max(best, length)
    return best


def subarray_sum_k(nums: List[int], k: int) -> int:
    """Count subarrays summing to k. O(n).
    >>> subarray_sum_k([1,1,1], 2)
    2
    """
    prefix = {0: 1}
    total = count = 0
    for n in nums:
        total += n
        count += prefix.get(total - k, 0)
        prefix[total] = prefix.get(total, 0) + 1
    return count


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """Top k frequent (bucket sort). O(n).
    >>> top_k_frequent([1,1,1,2,2,3], 2)
    [1, 2]
    """
    count = Counter(nums)
    buckets: List[List[int]] = [[] for _ in range(len(nums) + 1)]
    for n, f in count.items():
        buckets[f].append(n)
    res: List[int] = []
    for i in range(len(buckets) - 1, -1, -1):
        res.extend(buckets[i])
        if len(res) >= k:
            break
    return res[:k]


def find_duplicates(nums: List[int]) -> List[int]:
    """Find all duplicates in array (values 1..n). O(n) in-place.
    >>> find_duplicates([4,3,2,7,8,2,3,1])
    [2, 3]
    """
    res: List[int] = []
    for n in nums:
        i = abs(n) - 1
        if nums[i] < 0:
            res.append(abs(n))
        else:
            nums[i] = -nums[i]
    return res


class LRUCache:
    """LRU Cache — O(1) get and put. Uses OrderedDict.
    >>> lru=LRUCache(2); lru.put(1,1); lru.put(2,2); lru.get(1)
    1
    """

    def __init__(self, capacity: int) -> None:
        from collections import OrderedDict

        self.cap = capacity
        self.cache: "OrderedDict[int,int]" = __import__("collections").OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)


def two_sum(nums: List[int], target: int) -> Optional[List[int]]:
    """Two sum with hash map. O(n).
    >>> two_sum([2,7,11,15], 9)
    [0, 1]
    """
    seen: dict = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target - n], i]
        seen[n] = i
    return None


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """Group anagrams. O(n*k logk).
    >>> len(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
    3
    """
    groups: dict = defaultdict(list)
    for s in strs:
        groups[tuple(sorted(s))].append(s)
    return list(groups.values())


def ransom_note(ransom: str, magazine: str) -> bool:
    """Can construct ransom note from magazine. O(n).
    >>> ransom_note("aa","aab")
    True
    """
    mag = Counter(magazine)
    for c in ransom:
        if mag[c] <= 0:
            return False
        mag[c] -= 1
    return True


class TwoSum:
    """Data structure supporting add and find(target).
    >>> ts=TwoSum(); ts.add(1); ts.add(3); ts.add(5); ts.find(4)
    True
    """

    def __init__(self) -> None:
        self.nums: dict = {}

    def add(self, n: int) -> None:
        self.nums[n] = self.nums.get(n, 0) + 1

    def find(self, t: int) -> bool:
        for n in self.nums:
            comp = t - n
            if comp in self.nums and (comp != n or self.nums[n] > 1):
                return True
        return False


if __name__ == "__main__":
    print("Contains dup:", contains_duplicate([1, 2, 3, 1]))
    print("Longest consec:", longest_consecutive([100, 4, 200, 1, 3, 2]))
    print("Subarray sum k=2:", subarray_sum_k([1, 1, 1], 2))
    print("Top 2 frequent:", top_k_frequent([1, 1, 1, 2, 2, 3], 2))
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print("LRU get 1:", lru.get(1))
    lru.put(3, 3)
    print("LRU get 2 (evicted):", lru.get(2))
    print("Two sum:", two_sum([2, 7, 11, 15], 9))
