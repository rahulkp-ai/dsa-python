"""
Module: math_utils.py  Topic: Math Algorithms
GCD, LCM, Sieve of Eratosthenes, prime check, fast pow,
Fibonacci matrix, combinatorics, modular arithmetic.
"""

from typing import List


def gcd(a: int, b: int) -> int:
    """Greatest Common Divisor (Euclidean). O(logn).
    >>> gcd(48, 18)
    6
    >>> gcd(4, -6)
    2
    """
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Least Common Multiple. O(logn).
    >>> lcm(4, 6)
    12
    >>> lcm(4, -6)
    12
    """
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


def sieve_of_eratosthenes(n: int) -> List[int]:
    """All primes <= n. O(n loglogn).
    >>> sieve_of_eratosthenes(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    """
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(2, n + 1) if is_prime[i]]


def is_prime(n: int) -> bool:
    """Primality test. O(sqrt(n)).
    >>> is_prime(17)
    True
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def power_mod(base: int, exp: int, mod: int) -> int:
    """Modular fast exponentiation. O(logn).
    >>> power_mod(2, 10, 1000)
    24
    """
    result = 1
    base %= mod
    while exp > 0:
        if exp & 1:
            result = result * base % mod
        base = base * base % mod
        exp >>= 1
    return result


def factorial_mod(n: int, mod: int) -> int:
    """n! mod p. O(n).
    >>> factorial_mod(10, 1000000007)
    3628800
    """
    result = 1
    for i in range(2, n + 1):
        result = result * i % mod
    return result


def nCr_mod(n: int, r: int, mod: int) -> int:
    """C(n,r) mod p using Lucas / precomputed factorials. O(n).
    >>> nCr_mod(10, 3, 1000000007)
    120
    """
    if r > n:
        return 0
    num = den = 1
    for i in range(r):
        num = num * (n - i) % mod
        den = den * (i + 1) % mod
    return num * power_mod(den, mod - 2, mod) % mod


def count_digits(n: int) -> int:
    """Count digits in n. O(logn).
    >>> count_digits(12345)
    5
    """
    if n == 0:
        return 1
    count = 0
    while n:
        n //= 10
        count += 1
    return count


def digit_sum(n: int) -> int:
    """Sum of digits. O(logn).
    >>> digit_sum(123)
    6
    """
    return sum(int(d) for d in str(abs(n)))


def reverse_number(n: int) -> int:
    """Reverse digits of integer. O(logn).
    >>> reverse_number(123)
    321
    """
    sign = -1 if n < 0 else 1
    n = abs(n)
    rev = int(str(n)[::-1])
    result = sign * rev
    return result if -(2**31) <= result <= 2**31 - 1 else 0


def is_perfect_square(n: int) -> bool:
    """Check perfect square. O(logn).
    >>> is_perfect_square(16)
    True
    """
    if n < 0:
        return False
    root = int(n**0.5)
    return root * root == n


def nth_fibonacci_matrix(n: int) -> int:
    """Nth Fibonacci via matrix exponentiation. O(logn).
    >>> nth_fibonacci_matrix(10)
    55
    """

    def mat_mul(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        return [
            [
                A[0][0] * B[0][0] + A[0][1] * B[1][0],
                A[0][0] * B[0][1] + A[0][1] * B[1][1],
            ],
            [
                A[1][0] * B[0][0] + A[1][1] * B[1][0],
                A[1][0] * B[0][1] + A[1][1] * B[1][1],
            ],
        ]

    def mat_pow(M: List[List[int]], p: int) -> List[List[int]]:
        if p == 1:
            return M
        if p % 2 == 0:
            half = mat_pow(M, p // 2)
            return mat_mul(half, half)
        return mat_mul(M, mat_pow(M, p - 1))

    if n <= 1:
        return n
    M = [[1, 1], [1, 0]]
    result = mat_pow(M, n)
    return result[0][1]


if __name__ == "__main__":  # pragma: no cover
    print("GCD(48,18):", gcd(48, 18))
    print("LCM(4,6):", lcm(4, 6))
    print("Primes to 30:", sieve_of_eratosthenes(30))
    print("is_prime(17):", is_prime(17))
    print("2^10 mod 1000:", power_mod(2, 10, 1000))
    print("C(10,3):", nCr_mod(10, 3, 10**9 + 7))
    print("Digit sum(123):", digit_sum(123))
    print("Fib(10) matrix:", nth_fibonacci_matrix(10))
