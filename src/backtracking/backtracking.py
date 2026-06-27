"""
Module: backtracking.py  Topic: Backtracking
N-Queens, Sudoku, Permutations, Combinations, Subsets,
Word Search, Letter Combinations, Palindrome Partition.
"""

from typing import List


def solve_n_queens(n: int) -> List[List[str]]:
    """N-Queens. O(n!) time. All valid board configs.
    >>> len(solve_n_queens(4))
    2
    """
    res: List[List[str]] = []
    cols: set = set()
    d1: set = set()
    d2: set = set()
    queens: List[int] = []

    def bt(row: int) -> None:
        if row == n:
            board = ["." * q + "Q" + "." * (n - q - 1) for q in queens]
            res.append(board)
            return
        for col in range(n):
            if col in cols or row - col in d1 or row + col in d2:
                continue
            queens.append(col)
            cols.add(col)
            d1.add(row - col)
            d2.add(row + col)
            bt(row + 1)
            queens.pop()
            cols.remove(col)
            d1.remove(row - col)
            d2.remove(row + col)

    bt(0)
    return res


def permutations(nums: List[int]) -> List[List[int]]:
    """All permutations. O(n*n!) time.
    >>> len(permutations([1,2,3]))
    6
    """
    res: List[List[int]] = []

    def bt(cur: List[int], rem: List[int]) -> None:
        if not rem:
            res.append(cur[:])
            return
        for i in range(len(rem)):
            cur.append(rem[i])
            bt(cur, rem[:i] + rem[i + 1 :])
            cur.pop()

    bt([], nums)
    return res


def combinations(n: int, k: int) -> List[List[int]]:
    """All C(n,k) combinations from 1..n.
    >>> len(combinations(4,2))
    6
    """
    res: List[List[int]] = []

    def bt(start: int, cur: List[int]) -> None:
        if len(cur) == k:
            res.append(cur[:])
            return
        for i in range(start, n + 1):
            if n - i + 1 < k - len(cur):
                break
            cur.append(i)
            bt(i + 1, cur)
            cur.pop()

    bt(1, [])
    return res


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """Combinations summing to target (elements reusable).
    >>> combination_sum([2,3,6,7], 7)
    [[2, 2, 3], [7]]
    """
    candidates.sort()
    res: List[List[int]] = []

    def bt(start: int, cur: List[int], rem: int) -> None:
        if rem == 0:
            res.append(cur[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > rem:
                break
            cur.append(candidates[i])
            bt(i, cur, rem - candidates[i])
            cur.pop()

    bt(0, [], target)
    return res


def combination_sum_ii(candidates: List[int], target: int) -> List[List[int]]:
    """Combination sum with duplicates (each element used once)."""
    candidates.sort()
    res: List[List[int]] = []

    def bt(start: int, cur: List[int], rem: int) -> None:
        if rem == 0:
            res.append(cur[:])
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > rem:
                break
            cur.append(candidates[i])
            bt(i + 1, cur, rem - candidates[i])
            cur.pop()

    bt(0, [], target)
    return res


def subsets(nums: List[int]) -> List[List[int]]:
    """Power set - all subsets. O(2^n).
    >>> len(subsets([1,2,3]))
    8
    """
    res: List[List[int]] = []

    def bt(start: int, cur: List[int]) -> None:
        res.append(cur[:])
        for i in range(start, len(nums)):
            cur.append(nums[i])
            bt(i + 1, cur)
            cur.pop()

    bt(0, [])
    return res


def subsets_with_dup(nums: List[int]) -> List[List[int]]:
    """Subsets with possible duplicates (unique subsets)."""
    nums.sort()
    res: List[List[int]] = []

    def bt(start: int, cur: List[int]) -> None:
        res.append(cur[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            cur.append(nums[i])
            bt(i + 1, cur)
            cur.pop()

    bt(0, [])
    return res


def word_search(board: List[List[str]], word: str) -> bool:
    """Find word in grid. O(M*N*4^L) time.
    >>> word_search([["A","B","C"],["S","F","C"],["A","D","E"]], "ABCCED")
    True
    """
    rows, cols = len(board), len(board[0])

    def dfs(r: int, c: int, i: int) -> bool:
        if i == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
            return False
        tmp = board[r][c]
        board[r][c] = "#"
        found = (
            dfs(r + 1, c, i + 1)
            or dfs(r - 1, c, i + 1)
            or dfs(r, c + 1, i + 1)
            or dfs(r, c - 1, i + 1)
        )
        board[r][c] = tmp
        return found

    return any(dfs(r, c, 0) for r in range(rows) for c in range(cols))


def letter_combinations(digits: str) -> List[str]:
    """Phone digit letter combinations.
    >>> letter_combinations("23")
    ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    """
    if not digits:
        return []
    m = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    res: List[str] = []

    def bt(i: int, cur: List[str]) -> None:
        if i == len(digits):
            res.append("".join(cur))
            return
        for ch in m[digits[i]]:
            cur.append(ch)
            bt(i + 1, cur)
            cur.pop()

    bt(0, [])
    return res


def palindrome_partition(s: str) -> List[List[str]]:
    """All palindrome partitions of string."""
    res: List[List[str]] = []

    def is_pal(sub: str) -> bool:
        return sub == sub[::-1]

    def bt(start: int, cur: List[str]) -> None:
        if start == len(s):
            res.append(cur[:])
            return
        for end in range(start + 1, len(s) + 1):
            if is_pal(s[start:end]):
                cur.append(s[start:end])
                bt(end, cur)
                cur.pop()

    bt(0, [])
    return res


def solve_sudoku(board: List[List[str]]) -> bool:
    """Solve 9x9 Sudoku in-place."""

    def valid(r: int, c: int, num: str) -> bool:
        if num in board[r]:
            return False
        if num in [board[i][c] for i in range(9)]:
            return False
        br, bc = 3 * (r // 3), 3 * (c // 3)
        return not any(
            board[i][j] == num for i in range(br, br + 3) for j in range(bc, bc + 3)
        )

    def solve() -> bool:
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    for num in "123456789":
                        if valid(r, c, num):
                            board[r][c] = num
                            if solve():
                                return True
                            board[r][c] = "."
                    return False
        return True

    return solve()


if __name__ == "__main__":
    print("N-Queens(4):", len(solve_n_queens(4)), "solutions")
    print("Permutations:", permutations([1, 2, 3]))
    print("Combinations(4,2):", combinations(4, 2))
    print("Subsets:", subsets([1, 2, 3]))
    print("Combo Sum:", combination_sum([2, 3, 6, 7], 7))
    print("Letter combos '23':", letter_combinations("23"))
    print("Palindrome partitions 'aab':", palindrome_partition("aab"))
